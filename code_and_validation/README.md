# Code and validation materials

Frozen code archive, validation scripts and validation results for the Gold 411 and Silver 792 records. Frozen run: `ebook30_ocrseed_v2_seed2026081001`.

## Files

| File | Contents |
|---|---|
| `ocrseed_v2_code.tar.gz` | Frozen code archive (SHA-256 `32beb164…`). Contains `ebook_pipeline/` (PDF indexing, candidate detection and prefilter, sharded OCR workers, merging, audit), `common/formula_kb_production/` (OCR, formula parsing, M01–M12 rule implementation, structural indexing), `run_ebook30.sh`, `requirements.txt` and a README. |
| `gold_parser_recheck.py` | Rebuilds the typed formula tree and recomputes rule labels for the Gold records from archived OCR text, using the frozen engine. Argument driven; contains no local paths; does not rerun OCR. |
| `gold_parser_recheck.json` | Summary: 411 records, 411 matches on each of tree / analysis target / machine labels / human labels, 0 mismatches, engine SHA-256, Python version. |
| `gold_parser_recheck.csv` | The same comparison one row per record. |
| `compare_two_runs.py` | Compares the two host runs record by record on the fields it lists explicitly. It does not compare every field. |
| `runtime_addendum.json` | OCR weight identity and the rule used to compute its combined SHA-256, the Python environments used for the first run, the cross-host reproduction and the Gold recomputation, and a summary of the recomputation. |
| `LICENSE` | MIT license covering the code in this directory. |

## Reproducing the Gold recomputation

```bash
tar -xzf ocrseed_v2_code.tar.gz
python -I gold_parser_recheck.py \
    --gold ../gold_411/gold_records.jsonl \
    --engine-dir code/common/formula_kb_production/scripts \
    --out-dir out
```

The engine directory is the one that contains `formula_engine.py`; the script reads `machine_ocr_latex` from the Gold records and compares the rebuilt tree, the analysis target, the machine labels and the human labels against the archived values. Exit status is 0 when all four checks pass for every record.

## Scope and limits

- The recomputation shows that the archived OCR text reproduces the stored trees and rule labels with the frozen engine. It is a reproducibility check, not an independent judgement of the M01–M12 rules, and not a new round of human validation.
- `compare_two_runs.py` reports agreement on the fields it lists. Agreement of the outputs does not by itself establish agreement of inputs, weights or code across the two hosts.
- Original PDFs, page images and candidate crops are not included in this directory.
- OCR weight files are not redistributed; acquisition and verification are described in `runtime_addendum.json`.

## License

Code in this directory: MIT (see `LICENSE`). Dataset files in `gold_411/` and `silver_792/`: CC BY 4.0 (see the `LICENSE` file at the repository root).
