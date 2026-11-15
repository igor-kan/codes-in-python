# Gauss-Legendre Quadrature Node Engine (`gauss_legendre_nodes`)

> Category: **Numerical Quadrature** | Language: **Python 3.11+**

## Overview

Pure-Python Newton-Raphson Legendre root-finder generating symmetric Gauss-Legendre quadrature nodes and weights exact for degree <= 2n-1 polynomials.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(n^2)` |
| **Space Complexity** | `O(n)` |

## Mathematical & Safety Invariants

- nodes are strictly symmetric x[i] == -x[n-1-i] inside (-1, 1)
- weights sum exactly to 2.0 on [-1, 1]
- exact to machine precision on polynomials of degree up to 2n - 1

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
