# Linear-Space Hirschberg Levenshtein Alignment Recovery (`edit_distance_hirschberg_d60`)

> Category: **Dynamic Programming** | Language: **Python 3.11+**

## Overview

Recovers exact optimal Levenshtein alignment pairs between two strings in linear memory via divide-and-conquer midpoint DP splitting.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N * M) time and O(min(N, M)) recursion stack space` |
| **Space Complexity** | `O(M)` |

## Mathematical & Safety Invariants

- Aligned edit count matches full O(N * M) Levenshtein distance.

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
