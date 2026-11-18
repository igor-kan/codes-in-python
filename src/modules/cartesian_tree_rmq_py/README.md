# Linear-Time Stack Cartesian Tree & Range Minimum Query (`cartesian_tree_rmq_py`)

> Category: **Trees & RMQ** | Language: **Python 3.11+**

## Overview

Builds a min-heap Cartesian tree over an array in O(N) time using a monotonic stack and answers range minimum index queries via binary search descent.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N) monotonic right-spine construction + O(H) LCA range minimum` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- Every node index lies between its left and right subtrees and holds the range minimum.

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
