# O(N^3) Kuhn-Munkres Hungarian Linear Assignment (`hungarian_min_assignment_d56`)

> Category: **Combinatorial Optimization** | Language: **Python 3.11+**

## Overview

Solves square/rectangular minimum-cost bipartite linear assignment via Jonker-Volgenant potential updates in O(N^3) polynomial time.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N^3)` |
| **Space Complexity** | `O(N^2)` |

## Mathematical & Safety Invariants

- Assigned column indices are pairwise distinct and match brute-force permutation optimum.

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
