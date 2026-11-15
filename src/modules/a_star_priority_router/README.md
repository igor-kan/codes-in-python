# Admissible Grid A* Priority Router (`a_star_priority_router`)

> Category: **Graph Search / Pathfinding** | Language: **Python 3.11+**

## Overview

Four-neighbor weighted grid A* pathfinder with Manhattan consistent heuristic, closed-set optimality, and BFS tie-check oracle.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(E log V)` |
| **Space Complexity** | `O(V)` |

## Mathematical & Safety Invariants

- reported path begins at start and terminates at goal
- consecutive cells along path differ by Manhattan distance 1 and avoid obstacles
- consistent heuristic guarantees optimal shortest-path cost == Dijkstra cost

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
