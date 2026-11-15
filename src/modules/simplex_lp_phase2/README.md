# Tableau Simplex Linear Program Solver (`simplex_lp_phase2`)

> Category: **Mathematical Optimization** | Language: **Python 3.11+**

## Overview

Primal simplex tableau solver for standard inequality linear programs max c^T x s.t. A*x <= b, x >= 0 using Bland anti-cycling pivot selection.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(pivots * m * n)` |
| **Space Complexity** | `O(m * n)` |

## Mathematical & Safety Invariants

- every constraint holds: (A * x)_i <= b_i + 1e-9
- non-negativity x_j >= -1e-9 holds for all variables
- zero-reduced-cost optimality: all non-basic objective coefficients <= 1e-9

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
