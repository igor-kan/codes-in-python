# Exact Multi-Dimensional KD-Tree with Branch-and-Bound Nearest Neighbor (`kd_tree_nearest_py_d60`)

> Category: **Spatial Indexing** | Language: **Python 3.11+**

## Overview

Partitions K-dimensional Euclidean space via cyclic splitting planes and prunes subtrees when hypersphere radius cannot cross the split boundary.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N log N) median build and pruned nearest-neighbor search` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- Returned nearest point equals exhaustive linear scan distance.

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
