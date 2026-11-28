# SPFA Successive-Shortest-Path Min-Cost Flow Solver (`min_cost_flow_spfa_py_d61`)

> Category: **Network Flow** | Language: **Python 3.11+**

## Overview

Computes minimum-cost maximum flow by repeatedly finding the cheapest residual augmenting path with a queue-based Bellman-Ford relaxation that tolerates negative edge costs.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(F * V * E) queue-based shortest path augmentation` |
| **Space Complexity** | `O(V + E)` |

## Mathematical & Safety Invariants

- The reported flow equals the residual maximum and no negative-cost cycle remains.

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
