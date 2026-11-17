# Kahn Lexicographical DAG Topological Order & Path Counting DP (`topological_sort_all_paths`)

> Category: **Graph Algorithms** | Language: **Python 3.11+**

## Overview

Computes lexicographically smallest DAG topological sort using heapq zero-indegree scheduling alongside critical path length and exact s-t path multiplicity DP.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O((V + E) log V) min-heap order + O(V + E) path DP` |
| **Space Complexity** | `O(V + E)` |

## Mathematical & Safety Invariants

- Every edge u -> v respects order_pos[u] < order_pos[v].
- Cyclic graphs raise deterministic validation errors cleanly.

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
