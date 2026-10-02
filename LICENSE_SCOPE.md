# License scope

The [MIT License](LICENSE) covers project-owned Cell Painting Profile Explorer viewer/server code and documentation. The copyright notice is `Copyright (c) 2026 Cell Painting Profile Explorer contributors`. This grant is component-specific; it does not relicense the experiment or third-party material.

| Material | Scope |
| --- | --- |
| Root entry page, the viewer upload's `.gitignore`/`.gitattributes` and package metadata, viewer HTML/CSS/JavaScript, local server and package verifier | MIT for project-owned code and presentation; this category does not include scientific analysis configurations. |
| Viewer README and public documentation, original explanatory prose and viewer report templates | MIT for project-owned expression. Quoted notices, embedded source records, numerical tables and scientific content retain their separate status. |
| `explorer/sample-reports/*.html` | Mixed: project-owned HTML template/layout/prose is MIT; embedded saved numerical results, metadata, identities and JSON records are excluded from the project MIT grant. |
| `explorer/data.json`, `data.js`, `images.js`, `image-manifest.json`, `explorer/exports/**` and other saved scientific records | Excluded from the project MIT grant. No new data license or dedication is assigned here. Original upstream terms apply where applicable; retain their provenance and notices. The JavaScript data wrapper does not make the embedded data project-licensed software. |
| Original microscopy, PNG previews and scientific image/data content displayed in screenshots | Excluded from the project MIT grant. Gallery source data use CC0 as stated in the retained upstream notice. Preserve the exact source and display-transform provenance. |
| `assets/screenshots/**` | Mixed: the project-owned UI presentation is MIT; displayed scientific values, metadata and microscopy pixels are excluded from that grant. A screenshot is not a new scientific validation. |
| `notices/**` and other third-party material | Retain the exact applicable upstream terms. The project MIT file does not replace those notices. |
| Scientific execution code, copairs source/binaries, dependency runtimes, archived upstream helpers and archived execution material | Outside this viewer license grant and public-upload scope. This grant does not extend to excluded files. |

`LICENSE_SCOPE.json` in the upload package maps every payload path to a category and applicable notice paths. Mixed-file entries distinguish project-owned presentation from scientific content; they do not apply MIT to an entire exported table or sample record.

The retained [CPJUMP1 CC0 notice](notices/CPJUMP1-CC0.md), [CPJUMP1 BSD 3-Clause notice](notices/CPJUMP1-BSD-3-Clause.md) and [Gallery notice](notices/Cell-Painting-Gallery-LICENSE.txt) remain unchanged. The author repository assigns its source code BSD-3-Clause and its data/results/figures CC0; Gallery assigns its data CC0 and repository artifacts MIT. These scopes do not automatically cover newly generated scientific compilations or historical copairs copies.

Historical copairs exact-version scope and full runtime redistribution remain separate questions **only if those scientific sources/binaries are later distributed**. They are not blockers to this scoped MIT viewer package, which excludes them. See [third-party boundaries](docs/THIRD_PARTY_REDISTRIBUTION.md) and [the scientific-source boundary](docs/REPRODUCIBILITY.md).
