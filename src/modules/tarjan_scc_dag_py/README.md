# Iterative-Stack Tarjan Strongly Connected Components & Condensation DAG (`tarjan_scc_dag_py`)

> Category: **Graph Algorithms** | Language: **Python 3.11+**

## Overview

Computes Tarjan SCC decomposition and condensed DAG edges via explicit heap-allocated DFS call frames so deep directed graphs with > 10,000 chain nodes never exceed Python recursion limits.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(V + E) iterative (RecursionError-immune)` |
| **Space Complexity** | `O(V + E)` |

## Mathematical & Safety Invariants

- Every vertex u in 0..V-1 maps to exactly one strongly connected component ID.
- Condensed DAG edge (comp[u], comp[v]) obeys comp[u] > comp[v] (reverse topological postorder).

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
