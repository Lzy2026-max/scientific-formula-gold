# Gold dataset — 411 formula records

A formula dataset produced by directed review of 18 textbooks (340 pages). Each record carries the page-checked LaTeX transcription, the formula tree, the M01–M12 structural-pattern labels, and the frozen machine run (`ebook30_ocrseed_v2_seed2026081001`) output on the same formula, so the human standard and the machine result can be compared record by record.

## Dataset content

- **411 records, 411 unique `formula_id`, 399 distinct formula trees, 18 textbooks, 340 pages.**
- The set includes hard negatives whose machine labels are already correct; their machine tree fidelity is `passed` and core status is `valid_for_core_stats`, so they serve as "machine output is correct" controls.
- No `formula_id` is shared with the Silver 792 records. Three generic formula trees (`A x=b`, `x=A^{-1}b`, `y=A x+v`) also occur in Silver, but from different books/pages and independent typesetting; they are distinct records. For strict leakage isolation, group by tree.
- All 411 records have been recomputed with the frozen engine from the archived OCR text: formula tree, analysis target, machine M-labels and human M-labels each match 411/411. Recomputation material is in the sibling `code_and_validation/` directory.

## Files

| File | Contents |
|---|---|
| `gold_records.jsonl` | 411 records: human transcription, formula tree, M-labels, per-record review verdict and machine-comparison fields |
| `machine_formula_records.jsonl` | machine-side records from the frozen run (keyed by `formula_id`) |
| `machine_formula_trees.jsonl` | machine tree, analysis target, core status and machine M-labels from the frozen run |
| `schema.json` | definition of each field |
| `provenance.json` | source, composition and integrity information |
| `SHA256SUMS.txt` | file checksums |

## What you can do with it

- **Reference standard for formula parsing / OCR**: compare a system's output tree against `machine_tree_preorder` (reviewed as faithful to the page and reproducible from the archived OCR text), and its OCR/transcription against `human_transcription_latex`.
- **M-label evaluation**: use `human_m_labels` (M01–M12) as the reference to measure a labeling system's recall and false-positive rate.
- **Analysis-target evaluation**: `machine_analysis_target_preorder` gives the engine's analysis target on the faithful tree, for checking downstream symbolic-regression input extraction.
- **Hard negatives and calibration**: the hard-negative records ("machine labels already correct") test whether a system over-reports errors.
- **Generalization and leakage control**: `source_file` / `pdf_page_1based` allow splitting by textbook or page; `machine_tree_preorder` allows grouping by tree to keep the same formula off both sides of a train/test boundary.
- Records are annotated by textbook, page and formula structure, so the set works directly as a small-scale gold test set, or alongside the Silver 792 records (Silver provides the error-enriched samples; Gold provides the reference answers).

## Boundaries

- This is a **directed-review** collection, not a random sample; the counts describe this dataset only and must not be used as a denominator for overall accuracy or extrapolated to textbook-level precision.
- Review was single-person, item-by-item, with no cross-review; the labels are the M01–M12 structural-pattern set, not a complete error taxonomy.
- Source PDFs and page images are not distributed. `source_file`, `pdf_page_1based` and `source_pdf_sha256` allow the underlying page to be re-checked against the original edition.
- Machine fields come from parsing the archived OCR text; no OCR is rerun. The recomputation covers parsing, analysis target and labels, not independent human validation.
- `review_cohort` and `review_method` mark each record's review source and method; `human_m_node_witness` is optional and present only on some records.

## License

Data license: CC BY 4.0. See the `LICENSE` file at the repository root. Code in the sibling `code_and_validation/` directory is licensed under MIT.
