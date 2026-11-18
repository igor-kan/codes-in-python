# Hopcroft-Karp O(E sqrt(V)) Maximum Bipartite Matcher (`hopcroft_karp_bipartite_py`)

> Category: **Graph Matching** | Language: **Python 3.11+**

## Overview

Finds maximum cardinality bipartite matching by augmenting along all shortest vertex-disjoint augmenting paths per BFS distance layer.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(E * sqrt(V)) layered BFS + vertex-disjoint DFS augmenting paths` |
| **Space Complexity** | `O(V + E)` |

## Mathematical & Safety Invariants

- Matched left and right vertices form a valid bijection of maximum cardinality.

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
