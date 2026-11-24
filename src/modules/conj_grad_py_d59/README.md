# Pure-Python Conjugate Gradient SPD Linear Solver (`conj_grad_py_d59`)

> Category: **Numerical Linear Algebra** | Language: **Python 3.11+**

## Overview

Solves symmetric positive-definite linear equations A*x = b iteratively via orthogonal conjugate search directions without matrix factorization.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(K * N^2)` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- Solved residual norm ||A*x - b||_2 drops below 1e-9 cleanly.

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
