# Data and method provenance

The accepted experiment is `cpg0000-jump-pilot/source_4/2020_11_04_CPJUMP1`: parental A549, 5 µM compound exposure for 48 hours, baseline 1,000 seeded cells/well and no antibiotics. Plates BR00117015, BR00117016, BR00117017 and BR00117019 belong to one experiment/preparation.

## Sources

Chandrasekaran and colleagues / JUMP Cell Painting contributors supplied the experiment, profiles and published benchmark: [Nature Methods paper](https://www.nature.com/articles/s41592-024-02241-6) and [CPJUMP1 workflow at 6ba3fcd](https://github.com/jump-cellpainting/2024_Chandrasekaran_NatureMethods_CPJUMP1/tree/6ba3fcd1495d9e844e4607373a568641981ffcd8). Broad Institute / Cell Painting Gallery provides data distribution. John Arevalo and copairs contributors supplied the scientific pairing/retrieval implementation at [880f22a](https://github.com/cytomining/copairs/tree/880f22a551bd897896d148a0b07baa99d981c6a9). The viewer does not include copairs source or binaries.

Separate code paths and numerical checks support computational agreement, not independent peer review or biological validation. Upstream endorsement is not implied.

## Preserved result identities

There are 1,536 wells, 256 explicit negative controls, 1,280 final nonnegative queries and 306 scored source labels. DMSO is a separate control-only group with no final class mAP. The 125 chemical-key flags across 536 rows and 848 lossy PubChem metadata representations remain unchanged. Source IDs and control roles are not repaired by name matching.

All 15 registered variants and 17 contrasts remain visible. Paired means refer to exact common query IDs; own-population means are separate. Normalization N1/N2 versus N0 uses the same qualified base aggregates and 256-control fit; comparisons to author-processed REF are contextual. The installed deterministic reference reproduced the frozen baseline exactly; historical stochastic agreement retains its original conditional qualification.

Selection and filtering only change what is displayed. They do not generate new endpoints. [Methods](METHODS.md), [Findings](SCIENTIFIC_SYNTHESIS.md) and the [full result JSON](../explorer/exports/full-results.json) preserve the scientific definitions, exclusions and caveats.

## Four mapped microscopy previews

The packaged fields are BR00117015 A01/A02, site 1, DNA and RNA. A01 keeps its source treatment label; A02 has an explicit negative-control assignment and blank source sample ID, with DMSO only as the frozen reference's filled label. Other sample/well selections do not acquire a matched image by association.

[The image manifest](../explorer/image-manifest.json) retains the public TIFF object URLs, original/preview hashes, coordinates, source channel and exact display transforms. The source TIFFs are 1080 by 1080 uint16 images; their URLs and hashes are recorded in the manifest. PNG previews use independent 1st–99.5th percentile linear stretches, clipping and ties-to-even uint8 rounding. There is no crop, resize, rotation or invented scale bar. Brightness is not quantitatively comparable across previews and no treatment-effect conclusion is assigned.

## Notices and distribution

Preserve [CPJUMP1 CC0](../notices/CPJUMP1-CC0.md), [CPJUMP1 BSD 3-Clause](../notices/CPJUMP1-BSD-3-Clause.md) and [Gallery notice](../notices/Cell-Painting-Gallery-LICENSE.txt). CPJUMP1 notice acquisition uses revision `56845c7d4dc322652952783d91dae0ffef47829f`; the computational target stays at `6ba3fcd`. The Gallery notice was acquired at `5a954beeb0e27ba0b84f6557d813d40140605631`.

Project-owned viewer/server code and prose use the [MIT License](../LICENSE), within [License scope](../LICENSE_SCOPE.md). Data and third-party material retain their own notices. This repository contains the viewer and saved results, not the complete scientific execution package. See [Reproducibility](REPRODUCIBILITY.md) and [third-party notices](THIRD_PARTY_REDISTRIBUTION.md) for the exact versions and distribution boundaries.
