# Conjugate Gradient Symmetric Positive-Definite Linear System Solver (`conjugate_grad_py_d60`)

> Category: **Numerical Linear Algebra** | Language: **Python 3.11+**

## Overview

Solves A x = b for symmetric positive-definite matrices using mutually A-conjugate search directions until residual norm falls below tolerance.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(K * N^2) orthogonal residual minimization in N exact steps` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- Residual ||A x - b||_2 converges below 1e-10 for well-conditioned SPD matrices.

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
