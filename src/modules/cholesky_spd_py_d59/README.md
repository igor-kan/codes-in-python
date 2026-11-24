# Lower-Triangular Cholesky Decomposition L * L^T (`cholesky_spd_py_d59`)

> Category: **Matrix Factorizations** | Language: **Python 3.11+**

## Overview

Computes exact positive-diagonal lower-triangular factor L for symmetric positive-definite matrices satisfying L * L^T = A cleanly.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N^3 / 3)` |
| **Space Complexity** | `O(N^2)` |

## Mathematical & Safety Invariants

- Product L * L^T reconstructs every entry of A within 1e-10 tolerance.

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
