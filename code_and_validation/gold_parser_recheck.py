"""Recompute parse, analysis target and M-label results for all Gold records.

Usage:
  python -I gold_parser_recheck.py \
      --gold gold_records.jsonl \
      --engine-dir <extracted>/code/common/formula_kb_production/scripts \
      --out-dir .

The input records must contain machine_ocr_latex, machine_tree_preorder,
machine_analysis_target_preorder, machine_m_labels and human_m_labels.
No OCR is rerun; the archived OCR text is parsed with the frozen engine.

Outputs gold_parser_recheck.json (summary) and gold_parser_recheck.csv
(per-record comparison) in --out-dir.
"""
import argparse
import csv
import hashlib
import json
import sys
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--gold', required=True, help='Gold JSONL path')
    ap.add_argument('--engine-dir', required=True,
                    help='directory containing formula_engine.py')
    ap.add_argument('--out-dir', required=True, help='output directory')
    a = ap.parse_args()

    engine_dir = Path(a.engine_dir).resolve()
    sys.path.insert(0, str(engine_dir))
    import formula_engine as fe  # noqa: E402

    gold_path = Path(a.gold)
    rows = [json.loads(s) for s in gold_path.read_text(encoding='utf-8').splitlines() if s.strip()]

    rr = []
    for x in rows:
        n, t, d = fe.parse_formula_with_ocr_fallback(x['machine_ocr_latex'])
        target, legacy, pr = fe.classify(t)
        tags = sorted(q[:3] for q in pr['formula_level_tags'])
        rr.append({
            'formula_id': x['formula_id'],
            'review_id': x['review_id'],
            'tree_matches': t.preorder() == x['machine_tree_preorder'],
            'target_matches': target.preorder() == x['machine_analysis_target_preorder'],
            'tags_match': tags == sorted(x['machine_m_labels']),
            'human_tags_match': tags == sorted(x['human_m_labels']),
        })

    out = Path(a.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    summary = {
        'records': len(rr),
        **{k: sum(x[k] for x in rr) for k in
           ['tree_matches', 'target_matches', 'tags_match', 'human_tags_match']},
        'python': sys.version.split()[0],
        'formula_engine_sha256': hashlib.sha256(
            (engine_dir / 'formula_engine.py').read_bytes()).hexdigest(),
        'scope': ('parse and rule recomputation for all %d Gold records from '
                  'archived OCR text; no OCR rerun or independent human validation'
                  % len(rr)),
    }
    (out / 'gold_parser_recheck.json').write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    with (out / 'gold_parser_recheck.csv').open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rr[0]))
        w.writeheader()
        w.writerows(rr)

    fails = [x for x in rr if not all(x[k] for k in
             ['tree_matches', 'target_matches', 'tags_match', 'human_tags_match'])]
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print('FAILS', len(fails))
    for x in fails[:20]:
        print(x)
    return 1 if fails else 0


if __name__ == '__main__':
    raise SystemExit(main())
