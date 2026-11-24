# Floyd-Warshall Matrix Shortest Paths & Neg-Cycle Guard (`floyd_apsp_py_d59`)

> Category: **All-Pairs Shortest Paths** | Language: **Python 3.11+**

## Overview

Relaxes dense N x N directed distance matrices via intermediate vertex k loops and inspects main diagonals for negative cycle flags.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(V^3)` |
| **Space Complexity** | `O(V^2)` |

## Mathematical & Safety Invariants

- Negative cycle detection returns True iff diagonal entries turn negative cleanly.

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
