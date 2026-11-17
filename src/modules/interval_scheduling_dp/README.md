# Weighted Interval Scheduling (Binary Search Predecessor + Trace) (`interval_scheduling_dp`)

> Category: **Dynamic Programming** | Language: **Python 3.11+**

## Overview

Maximizes total weight across pairwise non-overlapping intervals using end-time sorting, binary-search compatible predecessor indexing, and DP optimal subset reconstruction.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N log N) end-time sort & bisect predecessor DP` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- Selected intervals are pairwise disjoint and sum to exact DP maximum weight.

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
