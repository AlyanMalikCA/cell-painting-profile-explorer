# Publish with GitHub Desktop

1. In **File > Options > Accounts**, sign in to the account that will own the finished project. Check your commit name/email under **Git**.
2. Choose **File > New repository**. Use `cell-painting-profile-explorer`, with no generated README, ignore template or license. Choose a folder outside any existing repository.
3. Select **Repository > Show in Explorer**. Copy this package's contents into that folder, keeping its folder structure. Use the supplied `.gitattributes`; keep the local `.git` directory.
4. Open `index.html`. Then run `python -B scripts/verify_public_candidate.py .` from the repository folder and confirm `"status": "PASS"`.
5. Commit with `Initial Cell Painting Profile Explorer release`. Select **Publish repository**, check the account/name, and choose the desired visibility.

The repository root should contain `index.html`, `README.md`, `LICENSE`, `.gitignore`, `.gitattributes`, `PUBLIC_FILES.json`, `CHECKSUMS.sha256`, the two license-scope files, and these folders:

```text
assets/
docs/
explorer/
notices/
scripts/
```

Do not upload ZIP archives, development workspaces, raw-data archives or runtime binaries. The included ignore rules help prevent accidental additions. Publication is separate from verifying the local package.
