# Dinic Level-Graph Blocking-Flow Solver in Python (`dinic_level_maxflow_py`)

> Category: **Network Flow** | Language: **Python 3.11+**

## Overview

Computes maximum s-t network flow using Dinic BFS distance layering and current-arc pointer DFS blocking flow.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(V^2 * E) BFS level graph + current-arc DFS augmentation` |
| **Space Complexity** | `O(V + E)` |

## Mathematical & Safety Invariants

- Total augmented flow equals minimum s-t cut capacity.

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
