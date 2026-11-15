# Capacity-Scaling Dinic Max-Flow (`ford_fulkerson_scaling`)

> Category: **Graph Optimization** | Language: **Python 3.11+**

## Overview

Dinic level-graph + capacity-scaling network flow solver verifying Max-Flow Min-Cut duality and per-vertex flow conservation.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(V * E log U)` |
| **Space Complexity** | `O(V + E)` |

## Mathematical & Safety Invariants

- every edge satisfies 0 <= flow <= capacity
- intermediate nodes maintain sum(inflow) == sum(outflow)
- total flow value equals exact s-t min-cut capacity in residual reachability

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
