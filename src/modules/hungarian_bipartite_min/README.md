# O(N^3) Potential-Based Rectangular Bipartite Minimum Assignment (`hungarian_bipartite_min`)

> Category: **Graph & Combinatorial Optimization** | Language: **Python 3.11+**

## Overview

Implements Jonker-Volgenant shortest augmenting path assignment with vertex dual potentials u[i], v[j] over arbitrary rectangular cost matrices, recovering optimal row-to-column permutation.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N^2 * M) for N <= M` |
| **Space Complexity** | `O(N + M)` |

## Mathematical & Safety Invariants

- Assigned column indices are pairwise distinct across all rows.
- Dual potentials satisfy u[i] + v[j] <= cost[i][j] everywhere and equality along matched pairs.

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
