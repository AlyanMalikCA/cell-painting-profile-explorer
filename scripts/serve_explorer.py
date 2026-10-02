"""Read-only local result viewer; standard library only, no scientific execution."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit, unquote, parse_qs
import argparse
import json
import hashlib
import mimetypes

HERE = Path(__file__).resolve()
ROOT = HERE.parents[1] if HERE.parent.name == 'scripts' else HERE.parents[2]
EXPLORER = ROOT / 'explorer'


def safe_relative(name):
    return (isinstance(name, str) and bool(name) and '\\' not in name and ':' not in name
            and '\x00' not in name and not name.startswith('/')
            and all(part not in ('', '.', '..') for part in name.split('/')))


def contained_file(base, relative):
    if not safe_relative(relative):
        return None
    candidate = base / relative
    try:
        candidate.resolve().relative_to(base.resolve())
        if candidate.is_file() and not candidate.is_symlink():
            return candidate
    except (OSError, ValueError):
        pass
    return None


def valid_data(data):
    return (isinstance(data, dict) and data.get('schema_version') == 1
            and isinstance(data.get('dataset'), dict)
            and isinstance(data['dataset'].get('plates'), list)
            and isinstance(data.get('reference'), dict)
            and isinstance(data.get('variants'), list) and bool(data['variants'])
            and isinstance(data.get('comparisons'), list) and bool(data['comparisons'])
            and isinstance(data.get('samples'), list) and bool(data['samples'])
            and all(isinstance(row, dict) and isinstance(row.get('id'), str)
                    and isinstance(row.get('name'), str) and isinstance(row.get('queries'), list)
                    and isinstance(row.get('scores'), dict) for row in data['samples']))


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(EXPLORER), **kwargs)

    def do_GET(self):
        return self.dispatch(False)

    def do_HEAD(self):
        return self.dispatch(True)

    def dispatch(self, head):
        url = urlsplit(self.path)
        path = unquote(url.path)
        if '\\' in path or '\x00' in path or any(part in ('.', '..') for part in path.split('/')):
            return self.send_error(404, 'Unknown local artifact')
        if path.startswith('/explorer/'):
            path = path[len('/explorer'):]
        if path == '/api/health':
            return self.send_json({'status': 'OK', 'mode': 'READ_ONLY_ARTIFACT_VIEWER',
                                   'scientific_execution': False, 'data_available': (EXPLORER / 'data.json').is_file()}, head=head)
        if path in ('/api/data', '/api/samples') or path.startswith('/api/sample/'):
            try:
                data = json.loads((EXPLORER / 'data.json').read_text(encoding='utf-8'))
                if not valid_data(data):
                    raise ValueError('Malformed viewer artifact')
            except (OSError, ValueError, TypeError):
                return self.send_json({'error': 'Verified result artifact unavailable or malformed; no placeholder data'}, 503, head)
            if path == '/api/data':
                return self.send_json(data, head=head)
            if path.startswith('/api/sample/'):
                identifier = path[len('/api/sample/'):]
                samples = [row for row in data['samples'] if row['id'] == identifier]
                return self.send_json(samples[0] if samples else {'error': 'Unknown frozen sample identity'}, 200 if samples else 404, head)
            needle = parse_qs(url.query).get('q', [''])[0].casefold()
            return self.send_json([row for row in data['samples'] if needle in (row['id']+' '+row['name']).casefold()], head=head)
        if path.startswith('/api/export/'):
            name = path[len('/api/export/'):]
            if not safe_relative(name) or len(PurePosixPath(name).parts) != 1:
                return self.send_error(404, 'Unknown shipped export')
            file = contained_file(EXPLORER / 'exports', name)
            return self.send_file(file, head) if file else self.send_error(404, 'Unknown shipped export')
        if path == '/':
            path = '/index.html'
        relative = path.lstrip('/')
        file = contained_file(EXPLORER, relative)
        if file:
            return self.send_file(file, head)
        # Explicit byte-bound documents only; never expose the workspace root.
        try:
            routes = json.loads((EXPLORER / 'document-routes.json').read_text(encoding='utf-8'))
            if not isinstance(routes, dict):
                raise ValueError('Malformed document route inventory')
            entries = routes.get('files', [])
            if not isinstance(entries, list) or len(entries) > 256:
                raise ValueError('Invalid document route inventory')
            rows = [row for row in entries if isinstance(row, dict) and row.get('path') == relative]
            if len(rows) == 1:
                row = rows[0]
                file = contained_file(ROOT, row['path'])
                if not file or row['bytes'] > 4 * 1024 * 1024:
                    raise ValueError('Unavailable declared document')
                raw = file.read_bytes()
                if len(raw) != row['bytes'] or hashlib.sha256(raw).hexdigest() != row['sha256']:
                    return self.send_error(503, 'Declared document differs from receipt; rebuild document routes')
                return self.send_file(file, head, raw)
        except (OSError, ValueError, KeyError, TypeError):
            pass
        return self.send_error(404, 'Unknown local artifact')

    def send_file(self, file, head=False, raw=None):
        try:
            body = file.read_bytes() if raw is None else raw
        except OSError:
            return self.send_error(404, 'Local artifact unavailable')
        self.send_response(200)
        mime = mimetypes.guess_type(file.name)[0] or 'application/octet-stream'
        if mime.startswith('text/') or mime in ('application/json', 'application/javascript'):
            mime += '; charset=utf-8'
        self.send_header('Content-Type', mime)
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        if not head:
            self.wfile.write(body)

    def send_json(self, value, status=200, head=False):
        body = (json.dumps(value, ensure_ascii=False, allow_nan=False) + '\n').encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        if not head:
            self.wfile.write(body)

    def end_headers(self):
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Referrer-Policy', 'no-referrer')
        return super().end_headers()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8785)
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error('Port must be in 1..65535')
    if not (EXPLORER / 'index.html').is_file() or not (EXPLORER / 'data.json').is_file():
        parser.error('Complete explorer build required; do not substitute data')
    server = ThreadingHTTPServer(('127.0.0.1', args.port), Handler)
    print(json.dumps({'status':'STARTED', 'url':f'http://127.0.0.1:{args.port}',
                      'title':'Cell Painting Profile Explorer','scientific_environment_modified':False}), flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == '__main__':
    main()
