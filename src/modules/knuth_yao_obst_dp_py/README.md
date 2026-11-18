# Knuth-Yao Quadrangle-Inequality Optimal Binary Search Tree DP (`knuth_yao_obst_dp_py`)

> Category: **Dynamic Programming Optimization** | Language: **Python 3.11+**

## Overview

Uses Knuth's root monotonicity opt[i][j-1] <= opt[i][j] <= opt[i+1][j] to compute optimal binary search tree cost in O(N^2) time.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N^2) monotonic root-table interval DP` |
| **Space Complexity** | `O(N^2)` |

## Mathematical & Safety Invariants

- Optimal cost matches cubic interval DP minimum.

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
