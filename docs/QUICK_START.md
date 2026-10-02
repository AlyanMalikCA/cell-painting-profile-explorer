# Quick start

## Open

Extract the folder and open [index.html](../index.html). The viewer works without an account, installation or internet connection. Keep the folders together.

With Python 3.10 or newer, an optional local server is available:

```sh
python -B scripts/serve_explorer.py --port 8785
```

Open `http://127.0.0.1:8785`. Press Ctrl+C in the terminal to stop the server.

## Explore

**Workbench:** search by name, source ID, chemical key or well. Filter by treatment/control role or identity flag. Select a sample in the left panel or a well on the plate; the right panel shows that selection's results. Use the plate selector to move between the four plates.

**Comparisons:** choose an analysis family, variant and comparator. Switch between score and rank plots. Selecting a point opens that sample's evidence. Paired means use the same common queries; the sample's overall mAP can differ.

**Microscopy:** four DNA/RNA previews cover plate BR00117015, wells A01 and A02, site 1. Other wells have no packaged image. Contrast is adjusted separately for each preview, so brightness is not comparable between images.

**Methods and Sources:** find calculation details, caveats, source versions and exports.

## Keyboard

Tab moves between controls. Within the plate, use arrow keys to select a neighboring well, Home/End for the start/end of a row, and Ctrl+Home/Ctrl+End for a plate corner. Keyboard focus is visible.

## Export

Use CSV/JSON for the full-precision numbers. Sample JSON and HTML reports include all saved variants and explicit exclusions. Filtering changes the display, not the calculated results. Controls and unassessable values are never substituted with zero.

## Verify the package

From this folder, run:

```sh
python -B scripts/verify_public_candidate.py .
```

A passing result checks file hashes, local links, source-bound reports, image receipts and license mapping. It does not rerun the scientific analysis. See [Reproducibility](REPRODUCIBILITY.md).
