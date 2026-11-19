# Kuhn-Munkres O(N^3) Hungarian Minimum-Cost Assignment (`hungarian_assign_o_n3_py`)

> Category: **Combinatorial Optimization** | Language: **Python 3.11+**

## Overview

Computes minimum-weight perfect bipartite assignment via O(N^3) Johnson potential updates in pure Python.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N^3) dual-potential shortest augmenting path match` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- Optimal primal cost equals negative sum of dual potentials -v[0].

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
