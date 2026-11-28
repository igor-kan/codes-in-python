# Bitmask N-Queens Solution Counter and First Placement (`nqueens_bitset_py_d61`)

> Category: **Constraint Search** | Language: **Python 3.11+**

## Overview

Counts all N-Queens placements and extracts one representative board using column, descending-diagonal, and ascending-diagonal bitmasks shifted per row instead of scanning the partial board.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N!) branch-and-bound with O(1) bitmask conflict tests` |
| **Space Complexity** | `O(N) recursion depth plus three bitmasks` |

## Mathematical & Safety Invariants

- Counts match the known N-Queens sequence and every returned board is conflict-free.

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
