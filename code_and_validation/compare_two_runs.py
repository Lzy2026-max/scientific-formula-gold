#!/usr/bin/env python3
"""Compare two isolated ebook runs without copying source text into the report."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path


FIELDS = {
    "formula_records.jsonl": (
        "formula_latex", "ocr_variant_latex", "ocr_status",
        "ocr_quality_status", "ocr_quality_reasons", "ocr_variant_similarity",
    ),
    "formula_trees.jsonl": (
        "formula_latex", "normalized", "tree_preorder", "record_status",
        "core_eligibility", "tags",
    ),
    "cluster_records.csv": (
        "formula_latex", "normalized", "tree_preorder", "validity_status",
        "is_core_formula", "m01_m12_tags", "fine_signature",
    ),
}


def sha256(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def read_selected(path: Path, fields: tuple[str, ...]) -> dict[str, tuple]:
    result = {}
    if path.suffix == ".csv":
        with path.open(encoding="utf-8-sig", newline="") as handle:
            rows = csv.DictReader(handle)
            for row in rows:
                key = str(row["formula_id"])
                if key in result:
                    raise ValueError(f"duplicate formula_id in {path}: {key}")
                result[key] = tuple(row.get(field) for field in fields)
    else:
        with path.open(encoding="utf-8-sig") as handle:
            for line in handle:
                if not line.strip():
                    continue
                row = json.loads(line)
                key = str(row["formula_id"])
                if key in result:
                    raise ValueError(f"duplicate formula_id in {path}: {key}")
                result[key] = tuple(row.get(field) for field in fields)
    return result


def compare_file(a: Path, b: Path, fields: tuple[str, ...]) -> dict:
    first = read_selected(a, fields)
    second = read_selected(b, fields)
    shared = first.keys() & second.keys()
    changes = Counter()
    changed_ids = set()
    for key in shared:
        for index, field in enumerate(fields):
            if first[key][index] != second[key][index]:
                changes[field] += 1
                changed_ids.add(key)
    return {
        "first_count": len(first),
        "second_count": len(second),
        "common_ids": len(shared),
        "first_only_ids": len(first.keys() - second.keys()),
        "second_only_ids": len(second.keys() - first.keys()),
        "changed_ids": len(changed_ids),
        "changed_fields": dict(changes),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-a", type=Path, required=True)
    parser.add_argument("--run-b", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    a, b = args.run_a.resolve(), args.run_b.resolve()
    report = {"index_sha256": {}, "audit_status": {}, "comparisons": {}}
    for label, run in (("a", a), ("b", b)):
        report["index_sha256"][label] = sha256(run / "index" / "candidate_index_all.jsonl")
        audit = json.loads((run / "official_results" / "audit_summary.json").read_text(encoding="utf-8"))
        report["audit_status"][label] = audit.get("audit_status")
    for name, fields in FIELDS.items():
        report["comparisons"][name] = compare_file(
            a / "official_results" / name,
            b / "official_results" / name,
            fields,
        )
    report["content_repeatable"] = (
        report["index_sha256"]["a"] == report["index_sha256"]["b"]
        and all(value == "PASS" for value in report["audit_status"].values())
        and all(
            item["first_only_ids"] == item["second_only_ids"] == item["changed_ids"] == 0
            for item in report["comparisons"].values()
        )
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.out), "content_repeatable": report["content_repeatable"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
