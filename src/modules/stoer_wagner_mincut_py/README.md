# Stoer-Wagner Global Undirected Min-Cut Solver in Python (`stoer_wagner_mincut_py`)

> Category: **Graph Cuts** | Language: **Python 3.11+**

## Overview

Computes the exact minimum cut of undirected weighted graphs via Stoer-Wagner vertex contraction phases.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(V^3) maximum-adjacency phase contraction` |
| **Space Complexity** | `O(V^2)` |

## Mathematical & Safety Invariants

- Global minimum cut weight <= every vertex weighted degree.

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
