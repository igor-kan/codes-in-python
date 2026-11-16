# Balanced Median-Split k-D Tree for Exact k-NN & Box Search (`kd_tree_nearest_py`)

> Category: **Spatial Data Structures** | Language: **Python 3.11+**

## Overview

Constructs a median-splitting k-D Tree over arbitrary D-dimensional float tuples with branch-and-bound k-Nearest Neighbors priority heap pruning and exact L2 squared distance verification.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N log N) build, O(log N) expected k-NN` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- k-NN returned distances are non-decreasing and match exhaustive O(N) Euclidean distance sort.
- Every box query point lies cleanly within inclusive coordinate bounds lo[d] <= p[d] <= hi[d].

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
