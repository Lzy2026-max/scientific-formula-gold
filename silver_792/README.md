# Silver dataset — 792 formula error records

A formula dataset drawn from an error-enriched review pool across 22 textbooks (617 pages). Each record carries the final LaTeX, the final formula tree, the M-label set, the frozen machine output it was compared against, and the per-record verdict. All records were verified item by item by a single reviewer; no independent cross-review was performed.

## What's in the dataset

| final_status | tree_verdict | records | meaning |
|---|---|---:|---|
| `usable` | `faithful` | 325 | tree faithful to the reviewed transcription; usable for training and as an evaluation reference |
| `train_only` | `faithful_source_merged` | 26 | tree faithful, but the source itself writes the symbols adjacent; labels kept for training only |
| `tree_distorted` | `broken` | 109 | the final tree still loses structure (see `loss_kinds`); not usable |
| `engine_gap` | `excluded_engine_gap` | 332 | the engine has no node for a construct in the formula and cannot emit a faithful tree; not usable |

- `usable_for_train`: 351 records (325 + 26).
- `usable_for_eval`: 325 records — a tree-quality flag, **not** a held-out split; every evaluation record is also in the training set. A disjoint held-out partition is provided in `splits/`.
- Empty label sets: 2 records carry the status `no_defect` and an empty label set; interpret this alongside the record-level evidence and status.
- Repeated formulas: 11 tree groups (24 records) share the same final tree; `tree_duplicate_group` marks them so trainers can group or deduplicate.

## Files

- `silver_records.jsonl` — 792 final records (schema in `schema.json`).
- `splits/silver_train_351.jsonl` — records with `usable_for_train = true` (eligibility file).
- `splits/silver_eval_325.jsonl` — records with `usable_for_eval = true` (eligibility file; subset of `silver_train_351.jsonl`).
- `splits/silver_train_heldout_283.jsonl` — disjoint training partition of the 351 eligible records.
- `splits/silver_test_heldout_68.jsonl` — disjoint held-out test partition (68 records, all `usable_for_eval`).
- `splits/split_manifest.json` / `splits/README.md` — split method, counts and checks.
- `machine_formula_records.jsonl` — machine-side fields from the frozen run, keyed by `formula_id`.
- `machine_formula_trees.jsonl` — machine tree, final tree and fidelity status, keyed by `formula_id`.
- `schema.json`, `provenance.json`, `SHA256SUMS.txt`.

## What you can do with it

- **Training data**: the 351 `usable_for_train` records provide transcription–tree–label triples for training formula parsing, tree prediction, or label prediction.
- **Evaluation reference**: the 325 `usable_for_eval` records give reference trees; use `splits/silver_train_heldout_283.jsonl` and `splits/silver_test_heldout_68.jsonl` as a ready train/test partition.
- **Error analysis**: `machine_record_note`, `defect_locus` and `loss_kinds` document where the frozen machine output failed (tree / OCR / label), so the set can drive error-recovery and robustness studies.
- **Controls**: the records whose machine labels were already correct are published in the Gold set, which can serve as "machine already correct" controls for calibration.

## Conventions

- `m_labels` records M01–M12 structural patterns matched by the formula tree. These labels describe structural patterns; machine errors are described separately by the diagnostic fields. Interpret empty labels using their accompanying status and evidence.
- `m_labels_origin` records how each label set was established during the single-reviewer verification: `human_verdict` marks an explicit item-by-item adjudication, and `tree_rule_derivation` marks the label set recorded during the reviewer's tree-level verification.
- `machine_record_note` documents the defect found in the **machine** record before repair; the final state of the published record is given by `tree_verdict`, `final_status`, `latex` and `tree_preorder`, not by that note.
- `tree_verdict_basis` records the verification stage at which the reviewer confirmed the tree verdict: page-level review, tree-level review, canonical-form review, structural-pattern review, or engine-gap review.

## Boundaries

- The records are an error-enriched subset, not a random sample. Counts here describe this review subset only and must not be read as book-level or dataset-level accuracy.
- Source PDFs and page images are not distributed. `source_file`, `pdf_page_1based` and `source_pdf_sha256` allow the underlying page to be re-checked against the original edition.
- Single-person review; no cross-review. Every record's transcription, tree and label set was verified item by item by the reviewer; 186 records additionally carry an explicit label-verdict note.
- No `formula_id` is shared with the Gold set (411 records). Three generic formula trees (`A x=b`, `x=A^{-1}b`, `y=A x+v`) also occur in Gold, but from different books/pages; they are independent records, not duplicates across the two sets.

## License

Data license: CC BY 4.0. See the `LICENSE` file at the repository root. Code in the sibling `code_and_validation/` directory is licensed under MIT.
