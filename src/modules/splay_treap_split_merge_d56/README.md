# Deterministic Seeded Treap Randomized BST (`splay_treap_split_merge_d56`)

> Category: **Balanced Search Trees** | Language: **Python 3.11+**

## Overview

Implements implicit-priority split/merge treaps supporting O(log N) rank order statistics, insertion, deletion, and range cardinality queries.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(log N) expected split and merge` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- In-order traversal always preserves strict ascending key sequence after splits/merges.

## Module Architecture

| File | Lifecycle Role |
| :--- | :--- |
| `models.py` | Stage 01 |
| `exceptions.py` | Stage 02 |
| `contract.py` | Stage 03 |
| `core.py` | Stage 04 |
| `validation.py` | Stage 05 |
| `fast_path.py` | Stage 06 |
| `concurrency.py` | Stage 07 |
| `invariants.py` | Stage 08 |
| `test_unit.py` | Stage 09 |
| `test_properties.py` | Stage 10 |
| `benchmark.py` | Stage 11 |
| `README.md` | Stage 12 |

## Verification & Execution Example

```text
python3 -m unittest test_unit.py test_properties.py && python3 benchmark.py
```

---
© 2026 Igor Kan
