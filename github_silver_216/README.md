# Silver diagnostic subset: 216 records

This folder contains 216 human reviewed Silver records aligned field by field to the frozen machine run `ebook30_ocrseed_v2_seed2026081001`. They were selected from a historical set of 251 records. The other 35 have changed machine outputs across versions and are excluded here. The 216 records do not overlap the 397 record Gold subset.

Silver records contain known or suspected errors and are intended for error analysis and repair. They are **not** ground truth for machine accuracy. Human M labels remain pending in some records; an empty `human_m_labels` list must be read with `human_m_status`.

## Files

- `silver_records.jsonl`: human review and machine fields for the 216 records. `prior_source_run_id` preserves the historical run; `source_run_id` names the frozen run.
- `machine_formula_records.jsonl`, `machine_formula_trees.jsonl`: corresponding raw outputs from the frozen run.
- `silver_review_216.csv`: compact human review table, one row per record.
- `alignment_audit_216.csv`: exact field alignment checks for the 216 selected records.
- `银子集汇总_216条_冻结版_2026-11-17.xlsx`: spreadsheet view of the compact review table.
- `manifest.json`: subset provenance and counts.
- `SHA256SUMS.txt`: checksums for these files.

Join files on `formula_id`; use `review_id` for the human review queue. The image paths in `silver_records.jsonl` are internal references and the images are not redistributed in this package. The existing Zenodo DOI for the full run and Gold subset does not archive this Silver addition.

Category counts: {"公式树": 116, "OCR": 61, "M标签": 39}.
