# Held-out split for Silver evaluation

`silver_train_heldout_283.jsonl` and `silver_test_heldout_68.jsonl` are a disjoint
partition of the 351 training-eligible records. The test file is drawn only from
the 325 evaluation-reference records; all 26 `train_only` records remain in the
training file.

Split rules (deterministic, no random seed):

- target test size per source book = max(1, round(0.2 x book evaluation-reference count));
- every `tree_duplicate_group` is assigned as a whole, so no duplicated formula
  tree crosses the train/test boundary;
- records are ordered by source file, page and candidate number.

The eligibility files `silver_train_351.jsonl` and `silver_eval_325.jsonl` are
**not** a train/test partition: all 325 evaluation-reference records are also in
the 351 training file. Use the held-out files for model evaluation.
