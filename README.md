# Scientific Textbook Formula Extraction Dataset

This repository provides formula records extracted from textbooks and monographs, together with curated Gold and Silver subsets and computational validation materials.

The frozen machine run is identified as `ebook30_ocrseed_v2_seed2026081001`. It contains 30,067 formula-tree records, including 2,289 records that meet the program-defined core criteria. Formula records link OCR text, expression trees, source locations, processing diagnostics and M01–M12 structural labels.

## Data access

The complete frozen machine output and the Gold and Silver subsets are archived on Zenodo:

**[Scientific Textbook Formula Extraction Dataset — Zenodo v3](https://doi.org/10.5281/zenodo.24425239)**

DOI: `10.5281/zenodo.24425239`

## Repository contents

| Directory | Contents |
|---|---|
| [`gold_411/`](gold_411/) | 411 Gold records, corresponding frozen machine records and trees, schema, provenance and checksums |
| [`silver_792/`](silver_792/) | 792 Silver diagnostic records, corresponding frozen machine outputs, schema, provenance and checksums |
| [`code_and_validation/`](code_and_validation/) | Frozen code archive and available computational validation materials |

### Gold subset

The Gold subset contains 411 formula records with transcriptions, structural labels, source locations and review evidence. Each record is linked to its corresponding frozen machine output by `formula_id`.

### Silver subset

The Silver subset contains 792 diagnostic records linking frozen machine outputs to reference information and evidence of differences in OCR, formula-tree parsing or M-label assignment. The records support error analysis and the study of how changes in formula structure affect rule-based labels.

Of these records, 351 are marked as eligible for training and 325 as eligible for use as evaluation references. The 325 evaluation-reference records are included in the 351 training-eligible records. Users should establish a separate partition when evaluating a model.

Gold and Silver have no overlapping `formula_id` values.

## Structural labels

M01–M12 are rule-based, potentially overlapping labels that describe structural patterns in formula trees, including variable relationships, function nesting and normalized subtree shapes. The label definitions combine structural properties discussed in prior research with the programmatic criteria used in this dataset.

## Reproducibility and source materials

Under the recorded configuration, outputs from two hosts were compared by formula identifier and selected fields. The available validation materials also include recomputation results for 397 Gold records from archived OCR text.

Source PDFs and page images are not distributed with the dataset. Source identifiers, PDF fingerprints, page numbers and region coordinates are provided to support source tracing.

## Citation

When using this dataset, please cite the Zenodo v3 record:

[https://doi.org/10.5281/zenodo.24425239](https://doi.org/10.5281/zenodo.24425239)
