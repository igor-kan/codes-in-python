# Kahn Lexicographic Topological Sort & DAG Longest-Path Solver (`topological_kahn_py_d60`)

> Category: **Graph Algorithms** | Language: **Python 3.11+**

## Overview

Computes the lexicographically smallest topological ordering of a DAG via min-heap zero-indegree scheduling and longest weighted path.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O((V + E) log V) min-heap Kahn + O(V + E) critical path` |
| **Space Complexity** | `O(V + E)` |

## Mathematical & Safety Invariants

- Raises ValidationError if a cycle prevents scheduling all V vertices.

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
