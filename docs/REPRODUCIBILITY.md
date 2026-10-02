# Reproducibility

This repository is a viewer of saved results. It needs no numerical Python dependencies; file-open operation needs only a supported browser, and its optional local server uses an existing Python 3.10+ standard library. It does not rerun the scientific pipeline.

The scientific calculation remains pinned to CPJUMP1 `6ba3fcd1495d9e844e4607373a568641981ffcd8`, copairs `880f22a551bd897896d148a0b07baa99d981c6a9` (0.0.3), Python 3.10.6, NumPy 1.23.4, pandas 1.5.1 and SciPy 1.9.3. Its 904-feature order, source labels, pair definitions and 100,000 null samples/query remain frozen. No later copairs or generic pipeline is substituted.

These are the exact published author-processed inputs. Git LFS pointer text is not the payload. A reproducibility run must verify the compressed-file SHA-256 before use; these profiles must not be treated as raw aggregates for new normalization.

| Plate | Published processed payload | SHA-256 |
|---|---|---|
| BR00117015 | [pinned input](https://media.githubusercontent.com/media/jump-cellpainting/2024_Chandrasekaran_NatureMethods_CPJUMP1/6ba3fcd1495d9e844e4607373a568641981ffcd8/profiles/2020_11_04_CPJUMP1/BR00117015/BR00117015_normalized_feature_select_negcon_batch.csv.gz) | `2102b4d0d8fd0135766bc9d2288d1a393b7fb84b1c71f8cafbe9f932037de565` |
| BR00117016 | [pinned input](https://media.githubusercontent.com/media/jump-cellpainting/2024_Chandrasekaran_NatureMethods_CPJUMP1/6ba3fcd1495d9e844e4607373a568641981ffcd8/profiles/2020_11_04_CPJUMP1/BR00117016/BR00117016_normalized_feature_select_negcon_batch.csv.gz) | `9fdf4b5d854b812a6562693f39a75d8b181ce86aed981048a664d110567d92fd` |
| BR00117017 | [pinned input](https://media.githubusercontent.com/media/jump-cellpainting/2024_Chandrasekaran_NatureMethods_CPJUMP1/6ba3fcd1495d9e844e4607373a568641981ffcd8/profiles/2020_11_04_CPJUMP1/BR00117017/BR00117017_normalized_feature_select_negcon_batch.csv.gz) | `9196b9dfac3dfdffb6cc7795abc55d0da7ee6426cf7559389b3091ba7b99b984` |
| BR00117019 | [pinned input](https://media.githubusercontent.com/media/jump-cellpainting/2024_Chandrasekaran_NatureMethods_CPJUMP1/6ba3fcd1495d9e844e4607373a568641981ffcd8/profiles/2020_11_04_CPJUMP1/BR00117019/BR00117019_normalized_feature_select_negcon_batch.csv.gz) | `db20a96f11f8dc0bf47df685dd43eb30244230545d77d795bee96c15004cf4fe` |

## What can be checked here

The viewer preserves source-bound values, sample identifiers, exclusions, input versions and byte hashes. The [source receipts](../explorer/exports/source-receipts.json) retain original analytical file paths as provenance identifiers, not as links to files included in this repository. The [package verifier](../scripts/verify_public_candidate.py) checks the viewer, reports, exports and image receipts.

## What is not included

The full scientific execution package, original input matrices and numerical runtime are not distributed here. Exact upstream links and versions do not by themselves provide an executable reproduction of this project's complete sensitivity workflow. Version-specific redistribution requirements for omitted code and binaries are documented under [third-party notices](THIRD_PARTY_REDISTRIBUTION.md).

Reference reproduction, stochastic qualification, descriptive sensitivity and presentation are distinct. Current saved values and scientific qualifications are available in [Methods](METHODS.md), [synthesis](SCIENTIFIC_SYNTHESIS.md), [provenance](PROVENANCE.md) and the shipped exports.

The [project MIT license](../LICENSE) covers only the project-owned viewer/server/documentation components listed in [LICENSE_SCOPE.md](../LICENSE_SCOPE.md). It does not license the omitted scientific execution package or relicense saved scientific outputs. The recorded scientific definitions and saved numerical outputs are unchanged.
