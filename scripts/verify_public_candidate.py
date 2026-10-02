"""Verify a technical-only viewer candidate using Python's standard library.

Owner-authorized MIT applies only to mapped project-owned portions. Verification never publishes files.
"""
from __future__ import annotations
import argparse
import hashlib
from html.parser import HTMLParser
import json
import posixpath
from pathlib import Path
import re
import stat
from urllib.parse import unquote, urlsplit
import zipfile

GENERATED = {"PUBLIC_FILES.json", "CHECKSUMS.sha256"}
PRIVATE = re.compile(r"(?i)(?:(?<![a-z0-9])[a-z]:[\\/]|/(?:home|Users|root|tmp|mnt)/)")
RULES = {
    "absolute_private_path": PRIVATE,
    "github_token": re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b"),
    "cloud_access_key": re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    "service_secret": re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{24,}\b"),
    "private_key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "credential_assignment": re.compile(r'''(?i)["']?(?:api_key|access_token|password|client_secret)["']?\s*[:=]\s*["'][^"'\s]{8,}["']'''),
}
SCRIPT_FILES = {"scripts/serve_explorer.py", "scripts/verify_public_candidate.py"}
SUFFIXES = {".html", ".js", ".css", ".json", ".csv", ".md", ".txt", ".png"}
REQUIRED = {"README.md", "LICENSE", "LICENSE_SCOPE.md", "LICENSE_SCOPE.json", "index.html", ".gitignore", ".gitattributes", "docs/GITHUB_DESKTOP_UPLOAD.md", "assets/screenshots/overview-workbench.png", "assets/screenshots/linked-treatment-image.png", "assets/screenshots/control-diagnostic.png", *SCRIPT_FILES, "explorer/index.html", "explorer/demo.html", "explorer/app.js", "explorer/styles.css",
            "explorer/data.json", "explorer/data.js", "explorer/images.js", "explorer/image-manifest.json",
            "explorer/document-routes.json", "explorer/METHODS.md", "explorer/ATTRIBUTION.md", "explorer/SCIENTIFIC_SYNTHESIS.md",
            "docs/QUICK_START.md", "docs/METHODS.md", "docs/SCIENTIFIC_SYNTHESIS.md", "docs/PROVENANCE.md", "docs/RELEASE_STATUS.md",
            "docs/THIRD_PARTY_REDISTRIBUTION.md", "notices/CPJUMP1-CC0.md", "notices/CPJUMP1-BSD-3-Clause.md", "notices/Cell-Painting-Gallery-LICENSE.txt"}


def require(value, message):
    if not value:
        raise ValueError(message)


def safe_name(name):
    require(isinstance(name, str) and name and "\\" not in name, "Unsafe public path")
    parts = name.split("/")
    for part in parts:
        require(part not in ("", ".", "..") and not part.endswith((" ", ".")), "Unsafe public path")
        require(not re.fullmatch(r"(?i)(?:CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(?:\..*)?", part), "Reserved public path")
        require(not any(ord(c) < 32 or c in ':<>"|?*' for c in part), "Unsafe public path")
    return name


def unique_names(names):
    seen = set()
    for name in names:
        safe_name(name)
        require(name.casefold() not in seen, "Duplicate or case-colliding public path")
        seen.add(name.casefold())
    for name in seen:
        parts = name.split("/")
        require(not any("/".join(parts[:i]) in seen for i in range(1, len(parts))), "File/directory collision")


def permitted(name):
    if any(part.casefold() == '.git' for part in name.split('/')):
        return False
    if name in SCRIPT_FILES or name in ("README.md", "LICENSE", "LICENSE_SCOPE.md", "LICENSE_SCOPE.json", "index.html", ".gitignore", ".gitattributes"):
        return True
    return name.startswith(("explorer/", "docs/", "notices/", "assets/screenshots/")) and Path(name).suffix.lower() in SUFFIXES


def scan_bytes(name, data):
    if name.endswith(".png"):
        require(data.startswith(b"\x89PNG\r\n\x1a\n"), "Preview file is not PNG")
        return []
    text = data.decode("utf-8-sig")
    findings = []
    for rule, pattern in RULES.items():
        for hit in pattern.finditer(text):
            # Never return a matched string, surrounding context, or secret value.
            findings.append({"path": name, "rule": rule, "line": text.count("\n", 0, hit.start()) + 1})
    return findings


def local_targets(name, raw):
    if name.endswith(".md"):
        links = re.findall(r"\]\(([^)]+)\)", raw.decode("utf-8"))
        links = [link.split(' "', 1)[0].strip().strip("<>") for link in links]
    elif name.endswith(".html"):
        links = re.findall(r'''(?:href|src)\s*=\s*["']([^"']+)["']''', raw.decode("utf-8"), re.I)
    else:
        return []
    targets = []
    for link in links:
        url = urlsplit(link)
        if url.scheme or url.netloc or not url.path:
            continue
        target = posixpath.normpath(posixpath.join(posixpath.dirname(name), unquote(url.path)))
        safe_name(target)
        targets.append(target)
    return targets


def checksum_bytes(rows, manifest_raw):
    hashes = {row["path"]: row["sha256"] for row in rows}
    hashes["PUBLIC_FILES.json"] = hashlib.sha256(manifest_raw).hexdigest()
    return "".join(f"{hashes[name]}  {name}\n" for name in sorted(hashes)).encode()


def verify_contents(read, names):
    unique_names(names)
    require(GENERATED.issubset(names), "Public inventory/checksums missing")
    raw = read("PUBLIC_FILES.json")
    manifest = json.loads(raw)
    require(manifest.get("schema_version") == 1 and manifest.get("kind") == "cell-painting-viewer-release", "Unexpected public inventory")
    require(manifest.get("publication_status") == "READY_FOR_OWNER_UPLOAD_NOT_PUBLISHED", "Release status must remain ready for owner upload, not published")
    rows = manifest["files"]
    paths = [row["path"] for row in rows]
    unique_names(paths)
    require(paths == sorted(paths) and len(rows) == manifest["file_count"], "Public inventory count/order differs")
    require(set(names) == set(paths) | GENERATED, "Missing or unexpected public files")
    require(REQUIRED.issubset(paths), "Required public viewer/server/document file missing")
    require(read("CHECKSUMS.sha256") == checksum_bytes(rows, raw), "Public checksums differ")
    findings, link_count = [], 0
    for row in rows:
        name = row["path"]
        require(permitted(name), "Excluded file category in public candidate: " + name)
        blob = read(name)
        require(len(blob) == row["bytes"] and hashlib.sha256(blob).hexdigest() == row["sha256"], "Public file hash/size differs: " + name)
        findings.extend(scan_bytes(name, blob))
        for target in local_targets(name, blob):
            require(target in paths, f"Missing public local link: {name} -> {target}")
            link_count += 1
    findings.extend(scan_bytes("PUBLIC_FILES.json", raw))
    require(not findings, "Public privacy scan failed: " + json.dumps(findings))
    verify_licenses(read, paths)
    data = json.loads(read("explorer/data.json"))
    for filename, prefix, expected in (("explorer/data.js", "window.CP_DATA=", data),
                                      ("explorer/images.js", "window.CP_IMAGES = ", json.loads(read("explorer/image-manifest.json")))):
        text = read(filename).decode("utf-8").replace("\r\n", "\n")
        require(text.startswith(prefix) and text.endswith(";\n") and json.loads(text[len(prefix):-2]) == expected,
                "Public browser/JSON payload differs: " + filename)
    require(len(data["samples"]) == 307 and len({row["id"] for row in data["samples"]}) == 307, "Sample count differs")
    require(len(data["variants"]) == 15 and len(data["comparisons"]) == 17, "Variant/comparison counts differ")
    reports = {"explorer/" + row["report_path"] for row in data["samples"]}
    require(len(reports) == 307 and reports == {name for name in paths if name.startswith("explorer/sample-reports/")}, "Public sample reports differ")
    verify_saved_reports(read, data)
    images = json.loads(read("explorer/image-manifest.json"))
    require(len(images["items"]) == 4, "Four selected image records required")
    for item in images["items"]:
        if item["status"] == "AVAILABLE":
            name = "explorer/" + item["display_path"]
            require(hashlib.sha256(read(name)).hexdigest() == item["display_sha256"], "Preview differs from image receipt")
    routes = json.loads(read("explorer/document-routes.json"))
    route_paths = [row["path"] for row in routes["files"]]
    unique_names(route_paths)
    require(set(route_paths) == {name for name in paths if name in ("README.md", "LICENSE", "LICENSE_SCOPE.md", "LICENSE_SCOPE.json") or name.startswith(("docs/", "notices/", "assets/screenshots/"))},
            "Public document routes contain missing or extra paths")
    for row in routes["files"]:
        blob = read(row["path"])
        require(len(blob) == row["bytes"] and hashlib.sha256(blob).hexdigest() == row["sha256"], "Public document route receipt differs")
    return {"status": "PASS", "publication_status": "READY_FOR_OWNER_UPLOAD_NOT_PUBLISHED", "file_count": len(rows),
            "sample_records": 307, "registered_variants": 15, "comparisons": 17, "image_records": 4,
            "local_links_verified": link_count, "privacy_findings": findings,
            "scope": "Viewer integrity, scoped owner-authorized MIT and privacy checks; ready for owner upload, not published; scientific execution excluded."}


class SavedReportParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.capture=False; self.values=[]; self.body=[]; self.executable=False
    def handle_starttag(self,tag,attrs):
        if tag=='script':
            attrs=dict(attrs)
            self.capture=attrs.get('id')=='saved-record' and attrs.get('type')=='application/json'
            if not self.capture:self.executable=True
            if self.capture:self.body=[]
    def handle_data(self,data):
        if self.capture:self.body.append(data)
    def handle_endtag(self,tag):
        if tag=='script' and self.capture:
            self.values.append(json.loads(''.join(self.body)));self.capture=False

def verify_saved_reports(read,data):
    for sample in data['samples']:
        name='explorer/'+sample['report_path']
        parser=SavedReportParser();parser.feed(read(name).decode('utf-8'))
        expected={'sample':sample,'variants':data['variants'],'comparisons':[
            {'id':c['id'],'role':c['role'],'pairs':[p for p in c['pairs'] if p['sample_id']==sample['id']]}
            for c in data['comparisons']]}
        require(not parser.executable and parser.values==[expected],'Saved report semantic payload differs: '+name)
    return len(data['samples'])


LICENSE_NOTICE = 'Copyright (c) 2026 Cell Painting Profile Explorer contributors'
NOTICE_PATHS = ['notices/CPJUMP1-CC0.md','notices/CPJUMP1-BSD-3-Clause.md','notices/Cell-Painting-Gallery-LICENSE.txt']

def license_category(name):
    if name.startswith('notices/'):return 'UPSTREAM_NOTICE'
    if name.startswith('explorer/assets/images/'):return 'UPSTREAM_IMAGE_CC0'
    if name.startswith(('explorer/sample-reports/','assets/screenshots/')):return 'MIXED'
    if name.startswith('explorer/exports/') or name in ('explorer/data.json','explorer/data.js','explorer/images.js','explorer/image-manifest.json'):
        return 'EXCLUDED_DATA'
    return 'MIT_PROJECT_OWNED_PORTIONS'

def license_map(names):
    scopes={
      'UPSTREAM_NOTICE':'Original upstream notice text, unchanged; not relicensed by this project.',
      'UPSTREAM_IMAGE_CC0':'Source image preview under applicable upstream CC0 provenance; no new MIT grant.',
      'MIXED':'Project-owned HTML/UI presentation is MIT; embedded or displayed scientific values, metadata and microscopy retain their separate upstream/data status.',
      'EXCLUDED_DATA':'Saved scientific values, metadata and exported result content excluded from the new project MIT grant; upstream CC0 where applicable.',
      'MIT_PROJECT_OWNED_PORTIONS':'MIT for project-owned code, prose and package metadata only; no grant over separately identified data or third-party material.'}
    return {'schema_version':1,'status':'OWNER_AUTHORIZED_MIT_SCOPED','owner_notice':LICENSE_NOTICE,
            'files':[{'path':n,'category':license_category(n),'license_scope':scopes[license_category(n)],
                      'notice_paths':NOTICE_PATHS if license_category(n)!='MIT_PROJECT_OWNED_PORTIONS' else ['LICENSE','LICENSE_SCOPE.md']}
                     for n in sorted(names)]}

def verify_licenses(read,paths):
    text=read('LICENSE').decode('utf-8')
    require(text.startswith('MIT License') and LICENSE_NOTICE in text and 'Permission is hereby granted, free of charge' in text,
            'Owner-authorized MIT notice missing or incorrect')
    expected=license_map(set(paths)|GENERATED)
    require(json.loads(read('LICENSE_SCOPE.json'))==expected,'Per-file license scope map differs or grants MIT to excluded data')
    require('scientific' in read('LICENSE_SCOPE.md').decode('utf-8').lower(),'Scoped license explanation missing')


def verify_directory(root):
    root = Path(root).resolve()
    names = []
    pending = [root]
    while pending:
        directory = pending.pop()
        for path in directory.iterdir():
            info = path.lstat()
            require(not stat.S_ISLNK(info.st_mode) and not getattr(info, "st_file_attributes", 0) & 0x400,
                    "Symlink/reparse point in public candidate")
            if path.name.casefold() == '.git':
                require(directory == root and path.name == '.git' and stat.S_ISDIR(info.st_mode),
                        "Only an ordinary root .git control directory may be excluded")
                # A local GitHub Desktop checkout adds repository-control metadata.
                # Never descend into it; this exception does not apply to ZIP entries.
                continue
            if stat.S_ISDIR(info.st_mode):
                pending.append(path)
            elif stat.S_ISREG(info.st_mode):
                names.append(path.relative_to(root).as_posix())
            else:
                raise ValueError('Unsupported file type in public candidate')
    return verify_contents(lambda name: (root / safe_name(name)).read_bytes(), sorted(names))


def verify_archive(path, expected_sha256=None):
    path = Path(path)
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if expected_sha256 is not None:
        require(digest == expected_sha256, "Public archive independent hash mismatch")
    with zipfile.ZipFile(path) as bundle:
        for info in bundle.infolist():
            require(not info.is_dir() and not info.flag_bits & 1 and not stat.S_ISLNK(info.external_attr >> 16), "Unsupported ZIP entry")
            require(info.orig_filename == info.filename, "ZIP normalized an unsafe path")
        result = verify_contents(bundle.read, bundle.namelist())  # every entry read, SHA and ZIP CRC checked
    result.update(archive_sha256=digest, archive_bytes=path.stat().st_size, external_hash_checked=expected_sha256 is not None)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--expected-sha256")
    args = parser.parse_args()
    result = verify_archive(args.path, args.expected_sha256) if args.path.is_file() else verify_directory(args.path)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
