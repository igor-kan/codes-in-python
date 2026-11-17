# Jacobi-Preconditioned Conjugate Gradient SPD Solver (`conjugate_gradient_dense`)

> Category: **Iterative Linear Algebra** | Language: **Python 3.11+**

## Overview

Solves dense symmetric positive-definite linear systems Ax = b in pure Python using Jacobi diagonal preconditioning and residual-norm stopping rules.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(K * N^2)` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- Relative residual ||Ax - b||_2 <= tol upon convergence.

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
