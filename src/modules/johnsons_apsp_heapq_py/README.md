# Johnson Potential-Reweighted Sparse All-Pairs Shortest Paths (`johnsons_apsp_heapq_py`)

> Category: **Shortest Paths** | Language: **Python 3.11+**

## Overview

Reweights sparse graphs with negative edges into non-negative instances via Bellman-Ford vertex potentials and executes heapq Dijkstra per source.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(V*E + V*E log V) Bellman-Ford reweighting + heapq Dijkstra` |
| **Space Complexity** | `O(V^2)` |

## Mathematical & Safety Invariants

- Shortest path distances equal exact negative-edge path weights cleanly.

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
