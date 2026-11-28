# Dancing Links Algorithm X Exact Cover Enumerator (`dancing_links_exact_cover_py_d61`)

> Category: **Constraint Search** | Language: **Python 3.11+**

## Overview

Solves the exact cover problem with Knuth's Algorithm X over a dancing-links matrix whose column headers track sizes and whose cover and uncover operations relink nodes in constant time.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(exponential search) with O(1) cover/uncover node relinking` |
| **Space Complexity** | `O(nodes) circular doubly-linked matrix` |

## Mathematical & Safety Invariants

- Each reported row set covers every column exactly once and never repeats a row.

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
