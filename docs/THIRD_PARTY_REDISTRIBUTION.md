# Third-party notices

The owner-approved [MIT license](../LICENSE) covers only the project-owned viewer/server code, presentation templates and documentation identified in [License scope](../LICENSE_SCOPE.md). It does not relicense scientific data or third-party work. The viewer-only package excludes the historical scientific implementation and binary runtimes; their conditional future review is not a blocker to this scoped viewer release.

## Preserved notices

| Notice | Retained upstream scope |
| --- | --- |
| [CPJUMP1 CC0](../notices/CPJUMP1-CC0.md) | Author data/results/figures, as declared by the archived author README. |
| [CPJUMP1 BSD 3-Clause](../notices/CPJUMP1-BSD-3-Clause.md) | Author repository source code, with notice retention and non-endorsement terms. This notice is retained for provenance; it does not imply the scientific source is shipped. |
| [Cell Painting Gallery](../notices/Cell-Painting-Gallery-LICENSE.txt) | Gallery data CC0 and Gallery repository artifacts MIT. |

These three notice files are retained byte-for-byte. CPJUMP1 notice acquisition is at `56845c7d4dc322652952783d91dae0ffef47829f`, while the computational target remains `6ba3fcd1495d9e844e4607373a568641981ffcd8`. Gallery notice acquisition is at `5a954beeb0e27ba0b84f6557d813d40140605631`. Exact image-source URLs, original/display hashes and contrast transforms remain in the image manifest.

## Mixed files and scientific content

Sample HTML reports combine a project-owned presentation template with saved scientific values and metadata. MIT covers the former, not the latter. JSON/CSV exports, data-bearing JavaScript, source metadata and saved numerical output are excluded from the project grant; no new data license or dedication is assigned by that grant. Genuine microscopy and its previews retain their upstream data scope. Application screenshots likewise combine project UI expression with separately scoped scientific data/pixels. Read the per-file `LICENSE_SCOPE.json` rather than treating every file beside LICENSE as wholly MIT.

## If scientific source or binaries are later published

The frozen copairs pin is `880f22a551bd897896d148a0b07baa99d981c6a9` (May 2023). Its source/wheel lacks its referenced license notice. Official copairs history [added BSD-3-Clause LICENSE in June 2024](https://github.com/cytomining/copairs/commit/d2e7cfd1bea3523d0c49630ec03d57d3f2cf793a); current copairs therefore is licensed, but applicability to this exact retained historical source and related helpers was not resolved by the bounded audit. No later dependency was silently substituted and no guessed license added to frozen archives.

Scientific wrappers, upstream helper/notebook copies, copairs source/binaries, dependency wheels and runtimes are absent from this viewer upload. A future distribution of them needs exact-version terms and complete bundled-component notices. Merely removing a wheel would not clear retained source copies; this viewer boundary excludes both. Those materials are not part of this distribution.

No paper PDF, review attachment, browser runtime or external design-library code is added to the viewer. Scientific/software sources are credited in [Provenance](PROVENANCE.md), without implying endorsement or independent peer review.
