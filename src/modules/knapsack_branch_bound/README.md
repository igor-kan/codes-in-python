# Exact 0/1 Knapsack Solver via Fractional-Bound Best-First Branch and Bound (`knapsack_branch_bound`)

> Category: **Combinatorial Optimization** | Language: **Python 3.11+**

## Overview

Solves exact 0/1 Knapsack problems using efficiency-sorted fractional linear relaxation upper bounds inside a priority queue with witness item reconstruction and DP equivalence validation.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(2^N) worst-case, strongly pruned via LP relaxation bounds` |
| **Space Complexity** | `O(N * active queue depth)` |

## Mathematical & Safety Invariants

- Total selected weight never exceeds configured capacity W.
- Recovered optimal value equals exact dynamic programming reference across random dense weights.

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
