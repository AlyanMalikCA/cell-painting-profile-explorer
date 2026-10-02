# Saved scientific synthesis: Cell Painting Profile Explorer

The frozen reference calculation reproduces the selected published task. The completed sensitivity grid shows that retrieval scores depend on representation and candidate eligibility within this four-plate experiment. High class-rank agreement can coexist with meaningful score changes. None of these results estimates a probability of biological reliability or establishes performance in another preparation.

This synthesis reads the existing results; it does not rescore profiles, refit normalization, change a baseline, or introduce another comparison. All **15 registered variants and 17 contrasts** completed. No variant was blocked, failed, substituted or selected for favorable results. All 17 class-rank summaries were assessable. The specific query exclusions below remain part of the result.

## Cohort and reference

The analytical cohort is A549 CPJUMP1, experiment `2020_11_04_CPJUMP1`, at the audited 5 µM/48-hour condition: plates `BR00117015`, `BR00117016`, `BR00117017` and `BR00117019`. There are **1,536 wells**, including **256 explicit negative controls**, **1,280 nonnegative queries**, and **306 source-sample labels**. Positive-control roles remain distinct and their source labels remain included. Four physical plates belong to one experiment/preparation; they are not four independent biological replications.

REF uses 904 ordered author-processed inputs, including the technical column `Cells_Parent_Nuclei`. Its inherited upstream feature-selection configuration includes a broader 51-plate population; this project imported fixed artifacts and did not reconstruct that fit. The analysis package reproduced all 1,536 reference query APs and 306 class means with zero numerical error against the fixed reference outputs. The earlier published stochastic comparison remains **conditional**, with its original scheduling and historical-query qualifications. It is not upgraded by the sensitivity results. See the [provenance summary](../docs/PROVENANCE.md).

## Reading the comparisons

AP measures how early source-defined positive candidates appear in a signed-cosine ranking relative to the eligible negatives. Class mAP is the arithmetic mean of eligible query APs for a source label. These are computational retrieval scores, not biological probabilities.

Every delta below is **variant minus comparator**, in raw AP units. Class summaries weight each common label equally. The comparator's class mean is recomputed on the **identical common query IDs**; full-population class means are separately retained. Mean absolute delta shows change without cancellation. Spearman uses average ranks of the exact saved class means. Values below are rounded for reading; [the complete comparison table](exports/comparisons.csv) and individual query/class exports retain full precision.

## Author-processed variants: primary comparisons with REF

| Variant | Candidates | Common queries / labels | Inputs | Mean class ΔAP | Mean absolute class ΔAP | Spearman |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Omit BR00117015 | 1,152 | 960 / 306 | 904 | -0.025971 | 0.040908 | 0.979859 |
| Omit BR00117016 | 1,152 | 960 / 306 | 904 | -0.013966 | 0.035979 | 0.979045 |
| Omit BR00117017 | 1,152 | 960 / 306 | 904 | -0.012145 | 0.035607 | 0.978260 |
| Omit BR00117019 | 1,152 | 960 / 306 | 904 | -0.026844 | 0.039981 | 0.979582 |
| Omit parent identifier | 1,536 | 1,280 / 306 | 903 | -0.000217 | 0.000436 | 0.999960 |
| Omit DNA features | 1,536 | 1,280 / 306 | 735 | +0.003144 | 0.020694 | 0.987311 |
| Omit ER features | 1,536 | 1,280 / 306 | 773 | +0.002270 | 0.012606 | 0.989275 |
| Omit RNA features | 1,536 | 1,280 / 306 | 759 | +0.005280 | 0.013461 | 0.989364 |
| Omit AGP features | 1,536 | 1,280 / 306 | 756 | -0.008264 | 0.019253 | 0.988957 |
| Omit Mito features | 1,536 | 1,280 / 306 | 774 | -0.021067 | 0.030230 | 0.986025 |
| Omit brightfield-family features | 1,536 | 1,280 / 306 | 602 | -0.007806 | 0.027788 | 0.983470 |
| Require different-position positives | 1,536 | 112 / 14 | 904 | -0.017643 | 0.017643 | 1.000000 |

Each plate omission removes 384 candidates: 320 final queries and 64 negative controls. All 306 labels remain represented, but the positive candidate counts and AP ranking problems change. Mean paired class AP decreases in all four branches, while rank correlations remain around 0.978–0.980. Both positive and negative class deltas occur; every branch has a zero median class delta. These are observed plate/candidate effects within this experiment, not estimates of a future batch's performance.

Removing the parent identifier produces a small average change and near-preserved class order. It is not an exact null effect: its class deltas range from -0.041667 to +0.013889. This technical-column sensitivity does not justify silently removing the column from the reproduced reference.

Channel removals have mixed directions. DNA, ER and RNA omission have positive mean class deltas; AGP, Mito and brightfield-family omission have negative mean deltas. Every channel branch contains both positive and negative class changes, and all have zero median class delta. This does not identify a better staining panel. Masks remove different numbers of columns and overlap through multichannel features; channel-agnostic segmentation and morphology remain. **There is no matched-size random-feature-removal control in this grid.** Dimensionality, overlap and the existing representation therefore cannot be separated from channel-associated measurement dependence. No physical stain was removed or image feature extraction repeated.

Different-position eligibility retains all 1,536 candidates but supports only 112 queries from 14 labels. The remaining **1,168 reference queries are unassessable for this question**, because they have no positive at another well coordinate; they are not assigned zero AP. The 14 class ranks are unchanged, yet mean class AP falls by 0.017643 and class deltas range from -0.241523 to 0. No positive class delta is observed in this subset. Spearman 1.0 therefore does not establish unchanged scores or absence of positional confounding, especially for the 292 labels outside this subset.

## Normalization: primary contrasts share the same aggregates

The four existing unnormalized aggregates were qualified separately. Exactly 256 explicit negative controls fit a common four-plate transformation; no treatment outcomes selected fit rows or features. The shared finite, positive SD/MAD mask retains **904/904** inputs and rejects none. All three branches use 1,536 candidates, 1,280 queries and 306 labels. N0 leaves those aggregate values unscaled; N1 uses pooled control mean/sample SD; N2 uses pooled control median/1.4826 MAD. See the [provenance summary](../docs/PROVENANCE.md).

| Primary contrast | Common queries / labels | Mean class ΔAP | Mean absolute class ΔAP | Spearman |
| --- | ---: | ---: | ---: | ---: |
| N1 z-score versus N0 | 1,280 / 306 | +0.151091 | 0.179419 | 0.809069 |
| N2 robust scaling versus N0 | 1,280 / 306 | +0.150509 | 0.177621 | 0.810945 |

Both transformations increase the mean class AP relative to the same unscaled inputs and substantially change class ordering. Neither improves every class: N1 class deltas range from -0.338320 to +0.911940; N2 from -0.310577 to +0.911940. Their mean deltas are similar, but this grid does not supply a prespecified N1-versus-N2 superiority test or independent biological validation. No preferred method is selected from these outcomes.

## Contextual contrasts with author-processed REF

| Contextual contrast | Common queries / labels | Mean class ΔAP | Mean absolute class ΔAP | Spearman |
| --- | ---: | ---: | ---: | ---: |
| N0 unscaled aggregates versus REF | 1,280 / 306 | -0.302497 | 0.306841 | 0.701679 |
| N1 z-score versus REF | 1,280 / 306 | -0.151406 | 0.151842 | 0.932297 |
| N2 robust scaling versus REF | 1,280 / 306 | -0.151988 | 0.152700 | 0.931870 |

These differences also change the input stage and inherited preprocessing history. They cannot be assigned solely to normalization or used to choose the upstream pipeline as biologically superior. Original object/site weighting, executed per-plate extraction details and calibrated physical units were not reconstructed; the qualified operation is a comparison on the same existing aggregate arrays.

## Uncertainty, precision and evidence

No new null samples, sensitivity p-values, q-values, fraction-retrieved endpoints, confidence intervals or bootstrap experiments were generated. All 17 Spearman summaries had sufficient nonconstant support; this does not remove the position-specific query exclusions. The [denominator overview](exports/full-results.json) and [excluded-query ledger](exports/full-results.json) retain exact populations and reasons. Source identity flags remain visible: 125 chemical-key conflicts across 536 rows and 848 lossy PubChem metadata representations were not repaired or used to redefine groups.

The pinned source puts positive candidates before negative candidates when constructing the rank list and preserves its observed positive-first behavior at exact similarity ties. AP ties were not randomized or given a new tie-averaged metric. This source reproduction convention can favor positives at exact ties and is not evidence of biological discrimination. Spearman is a separate calculation with average ranks for exact ties in saved class means. An audit-only alternative summation changed exact class ties in ten contrasts: affected means differed by at most 1.11e-16 and rho by at most 3.905e-5. Independent ranking of the **actual saved means** matches every registered rho exactly. No epsilon bins or alternative endpoints were adopted; small rank differences should not be overinterpreted.

Contract and statistical checks passed. A separate-code review recalculated all 16,752 saved variant query APs, all 17 comparisons and the reference, with zero AP error. The review artifacts and checksums were verified during report preparation; their scripts were not rerun for that report. The reported Linux numerical review does not establish cross-platform CLI support. These checks are not independent peer review or independent biological validation. See [Provenance](../docs/PROVENANCE.md).

Stain4, Stain5, Reagent1 and Scope remain provenance case studies only. They supplied no analytical matrices, fitting populations or validation endpoints here. No claim of causal compound action, therapeutic effect, toxicity, interlaboratory generalization or biological reliability percentage follows from this work.
