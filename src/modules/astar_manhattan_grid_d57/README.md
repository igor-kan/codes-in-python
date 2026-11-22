# A* Manhattan-Heuristic Shortest Grid Path Finder (`astar_manhattan_grid_d57`)

> Category: **Informed Graph Search** | Language: **Python 3.11+**

## Overview

Computes exact minimum hop distances across blocked 0/1 2D grids using an admissible L1 Manhattan heuristic priority queue.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O((R * C) log(R * C)) worst-case, admissible pruning` |
| **Space Complexity** | `O(R * C)` |

## Mathematical & Safety Invariants

- Returned optimal step count matches or beats BFS lower bound >= Manhattan(start, goal).

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
