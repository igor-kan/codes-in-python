# N-Dimensional Nelder-Mead Derivative-Free Simplex Optimizer (`nelder_mead_simplex_nd`)

> Category: **Nonlinear Optimization** | Language: **Python 3.11+**

## Overview

Minimizes arbitrary smooth or non-smooth N-dimensional scalar objectives via Nelder-Mead reflection, expansion, contraction, and full simplex shrink without gradients.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(Iters * N log N) simplex vertex evaluation & sort` |
| **Space Complexity** | `O(N^2) simplex vertex matrix` |

## Mathematical & Safety Invariants

- Simplex diameter and best objective decrease cleanly toward local minimum.

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
