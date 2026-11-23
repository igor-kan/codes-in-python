# 2D Spatial Quadtree Axis-Aligned Box Query Index (`quadtree_points_d58`)

> Category: **Spatial Indexing** | Language: **Python 3.11+**

## Overview

Recursively subdivides bounded 2D rectangular buckets whenever leaf capacity overflows to accelerate axis-aligned box queries.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N log B) insert, O(sqrt(N) + K) range query` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- Returned point counts strictly match naive box-containment filtering across points.

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
