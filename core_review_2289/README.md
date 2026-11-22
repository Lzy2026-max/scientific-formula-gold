# Core-layer review pool — 2,289 formula records

Per-record review of the complete core layer of the frozen run `ebook30_ocrseed_v2_seed2026081001`. The run produced 30,067 candidate formula trees; the 2,289 records with `core_eligibility == True` are the core layer. Each record carries the first failing stage of the extraction pipeline, the human review fields, the frozen machine output on the same formula, and a signature.

## Dataset content

- **2,289 records, 2,289 unique `formula_id`, 26 books, 1,576 book-page pairs.** `book_name` is the canonical title mapped from `source_file`; `book_title_as_recorded` keeps the value carried by the review queue.
- Composition: 1,812 records from the original queue, signed on 2026-11-12 to 2026-11-15; 231 blank queue rows and 246 core-only records (Q2283-Q2528) reviewed and signed on 2026-11-23. All 2,289 records were signed by Lzy.
- The 477 records reviewed on 2026-11-23 were checked one by one against the page context and the frozen OCR and tree; 109 first-pass judgments were corrected and 368 kept (confidence high 440, medium 37).
- First failing stage: none 448, formula tree 538, candidate identification 565, region completeness 400, OCR 222, M-labels and other 116 (M-labels 73 + target scope 26 + M-labels pending 14 + duplicate 3). Each record is counted once, at the earliest failing stage.
- The pool covers all 411 Gold records and 736 of the 792 Silver records. The remaining 56 Silver records are outside the frozen core layer and are not part of this pool.
- Three records are excluded from dataset scope by ruling: Q0173 and Q0284 (table cell constants) and Q2510 (a figure annotation). They are recorded as "no error" with `dataset_included = false`; the remaining 445 "no error" records can enter the dataset. Q2520 (an English quantifier in the tree) is ruled not a tree error and is included.

## Files

| File | Contents |
|---|---|
| `core_review_2289.jsonl` | 2,289 records: signature, first failing stage, human review fields, frozen machine fields, evidence note |
| `core_review_2289.xlsx` | Review workbook, 50 columns and 7 sheets (review_pool, notes, stage_statistics, coverage_check, frozen_recheck, item_review, scope_rulings) |
| `core_review_pie_2289.png` | First-failing-stage distribution (300 dpi) |
| `phase_distribution.csv` | The six reported bins with counts and percentages |
| `schema.json` | Definition of each field |
| `provenance.json` | Source, composition, counts, rulings and integrity information |
| `SHA256SUMS.txt` | File checksums |

## Language

This is the English rendering of the signed workbook. Sheet names, headers, stage names and verdicts are English. The reviewer's free-text evidence is kept verbatim in Chinese in fields whose name ends in `_zh` (`review_note_zh`, and the `_zh` columns of the workbook); `source_title`-style proper names are kept as recorded. Two workbook columns (`source_pdf_path_production`, `review_card_path_production` and the two image path columns) hold paths on the production machine, with the original Chinese folder names; neither the PDFs nor the images are distributed.

## What you can do with it

- **Pipeline diagnostics**: use `failure_stage` to measure where a formula-extraction pipeline fails first on a complete core layer, and to compare stages across systems on the same 2,289 records.
- **Review provenance**: `initial_failure_stage`, `stage_changed_after_item_review` and `review_note_zh` keep the first-pass judgment, the corrected judgment and the page evidence side by side.
- **Machine-output audit**: `machine_ocr_latex`, `machine_tree_preorder`, `machine_analysis_target` and `machine_m_labels` give the machine output each human verdict was passed on.
- **Coverage and leakage control**: the pool contains every Gold record and most Silver records, so it can serve as the common frame for both sets; split by `book_name`, `source_file` or tree to keep the same formula off both sides.
- **Workbook use**: open `core_review_2289.xlsx` for the full per-column review history and the four scope rulings.

## Boundaries

- This is a **directed review of a fixed core layer**, not a random sample; the counts describe these 2,289 records and must not be used as a denominator for overall accuracy.
- Review was single-person, item by item, with no cross-review. The `initial_failure_stage` column preserves the first-pass judgment even where the authoritative `failure_stage` differs.
- Source PDFs and page images are not distributed. `book_name`, `source_file`, `pdf_page` and `bbox_200dpi_px` allow the page to be re-checked against the original edition. Three records of `book_title_as_recorded` hold PDF metadata instead of a title; `book_name` is authoritative.
- Machine fields come from parsing the archived OCR text of the frozen run; no OCR was rerun.
- Three records are "no error" but out of dataset scope (`dataset_included = false`); quote 445, not 448, when counting records that can enter the dataset.

## License

Data license: CC BY 4.0. See the `LICENSE` file at the repository root.
