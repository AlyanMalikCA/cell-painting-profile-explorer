# Methods: Cell Painting Profile Explorer

Cell Painting Profile Explorer presents a reproduced retrieval calculation and its registered sensitivity comparisons. It helps readers trace a displayed result to a sample, a comparison population and a frozen result file. It does not diagnose cells or estimate drug effectiveness.

## What is in the explorer?

The dataset contains four A549 CPJUMP1 plates from experiment `2020_11_04_CPJUMP1`: `BR00117015`, `BR00117016`, `BR00117017` and `BR00117019`. The audited compound condition is 5 µM for 48 hours. These 1,536 wells include 256 explicit negative controls and 1,280 nonnegative query wells representing 306 source labels. Positive controls retain their source roles and are included in the source-defined final query population. Four plates from one preparation do not provide four independent biological replications.

The reference uses 904 ordered author-processed inputs. `Cells_Parent_Nuclei`, a technical identifier, remains included because it was selected upstream; its removal is a separate sensitivity branch. The broader upstream feature-selection configuration covered 51 plates. Importing that fixed representation does not mean its preprocessing was refitted or its complete execution history reconstructed here.

## What does AP measure?

For each eligible query, signed cosine similarity orders its allowed candidates. Positives are other rows with the same frozen source-sample label. Negatives come from the same physical plate and have the opposite explicit negative-control status. Self pairs are excluded. The reference does not require positives to have different well coordinates.

Average precision (AP) averages the precision of the ranking at the positions occupied by positives. Earlier positives give higher AP. A class mean averages AP across that source label's eligible queries. An AP of 0.9 is **not a 90% probability of biological reliability**, and a higher score is not proof of a beneficial drug effect.

The pinned source constructs positives before negatives and retains its positive-first behavior at exact similarity ties. That behavior is reproduced rather than replaced with randomized or tie-averaged AP; it can favor positives when similarities are exactly tied. The computational reference is pinned to workflow revision `6ba3fcd1495d9e844e4607373a568641981ffcd8` and copairs revision `880f22a551bd897896d148a0b07baa99d981c6a9`.

## How are changes compared?

All 15 registered sensitivity variants and 17 contrasts completed. The changes cover four plate omissions, one technical-column omission, six channel/family feature omissions, a different-position positive rule and three normalization branches.

The saved paired comparison matches identical global query IDs. Its recorded class means were computed on exactly those same queries before subtracting comparator from variant; the viewer reads these saved means without recalculating AP or class mAP. The separate population view shows each branch's own eligible class mean and member count. This prevents a change in population from being silently reported as a change in method on identical observations.

Spearman describes class-order agreement. It uses average ranks for exact ties in the saved class means. It would be unassessable with fewer than two common labels, a constant rank input or invalid values; there is no replacement statistic. All 17 executed rank comparisons were assessable. Tiny floating reduction changes can alter exact ties: an audit-only alternative summation shifted rho by up to 3.905e-5. The saved endpoint and its tie rule were not changed.

| Branch | What changes? | Population to notice |
| --- | --- | --- |
| Plate omission | One plate is removed from queries and candidates; no refit | 1,152 candidates, 960 paired queries, all 306 labels; 320 reference query exclusions |
| Technical/channel omission | Specified columns are removed; no refit | 1,536 candidates, 1,280 queries, 306 labels; input counts range from 602 to 903 |
| Different-position positives | Positives must have another well coordinate; negative rule unchanged | All 1,536 candidates remain, but only 112 queries and 14 labels are eligible; 1,168 queries are unassessable for this question |
| N0/N1/N2 normalization | Declared transforms of the same qualified aggregates | Shared 904 inputs, 1,536 candidates, 1,280 queries and 306 labels |

Different-position exclusions are not zero scores or evidence that the compounds lack effects. Channel masks overlap through multichannel features and remove unequal numbers of inputs. Segmentation-derived morphology remains, and no matched-size random-feature-removal control was run. These are feature-dependence comparisons, not physical stain-removal experiments or measures of unique channel importance.

## Why do normalization comparisons have two roles?

N0 leaves qualified unnormalized aggregate values unchanged. N1 subtracts the pooled negative-control mean and divides by sample SD (`ddof=1`). N2 subtracts the pooled negative-control median and divides by `1.4826 × raw MAD`. Only the 256 explicit controls fit these parameters. The shared mask requires finite, positive control SD and MAD; all 904 columns passed. No treatment outcomes, epsilon scales, clipping or imputation selected the transformation.

**N1 versus N0 and N2 versus N0 are the primary normalization comparisons.** They share the same input arrays, mask and populations. N0/N1/N2 versus the author-processed reference are contextual: their input stage and inherited preprocessing also change. A difference in those contextual comparisons cannot be attributed solely to normalization.

## What checks support the numbers?

The installed package reproduced the frozen reference APs and class means exactly. Metadata audits rebuilt candidate/query populations and pair masks; numerical audits checked saved deltas and ranks. A separate-code numerical review also recalculated all 15 variants. See the [scientific synthesis](SCIENTIFIC_SYNTHESIS.md) and [provenance summary](PROVENANCE.md). This viewer includes saved results and source receipts; the scientific execution package is not included.

The reference used 100,000 null samples per query and retains its original stochastic outputs and conditional publication comparison. The sensitivity analysis used saved counts and generated no new null draws, significance statistics or fraction-retrieved comparisons. No biological uncertainty interval, independent preparation validation or human peer-review certification is implied.

The frozen annotations retain 125 chemical-key conflicts across 536 rows and 848 lossy PubChem representations. Grouping uses exact source labels, not lossy IDs or inferred chemical names. External Stain4/Stain5/Reagent1/Scope records are provenance context only.

## Images and exports

An image is evidence for a particular plate, well, channel and site only when its mapping and source bytes have been checked. The microscopy view distinguishes four mapped experimental images from wells without a packaged image and shows each source and display transformation; no generated microscopy is substituted. A small image selection illustrates acquisition context; it does not validate all profiles or represent an unbiased biological survey.

Exports retain the chosen comparator, primary/contextual role, query/label counts, variant identifier, exact source IDs and provenance links. They report the saved calculation; browsing or exporting a result does not refit or rescore it. Read [Provenance](PROVENANCE.md) for source credits. These computational checks are not independent peer review or biological validation.

## Linked workbench views

The sample ledger, plate map and inspector refer to the same exact saved source IDs and physical plate/well coordinates. Selection and filtering change which evidence is visible; they do not change a candidate universe or refit a calculation. A well AP is a query result. Sample mAP averages the eligible queries for that label; paired-common-query means can differ from that sample's whole-population mean. The map's legend names its displayed saved quantity. Negative controls remain a distinct role, and missing or unassessable values are not assigned zero.

The source-value audit and 307 downloadable reports preserve all variants/comparisons and identity warnings. See [Quick start](QUICK_START.md) for keyboard navigation and exports. The [viewer-only distribution boundary](REPRODUCIBILITY.md) remains separate from scientific reproducibility and licensing clearance.

The workbench's code/documentation license is separate from scientific evidence. Read [License scope](../LICENSE_SCOPE.md) for the MIT-covered presentation and the excluded data/third-party content.
