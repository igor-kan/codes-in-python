# CLRS Red-Black Ordered Map (`rbtree_ordered_map`)

> Category: **Data Structures / Balanced Trees** | Language: **Python 3.11+**

## Overview

Left/right rotating CLRS Red-Black binary search tree ordered map guaranteeing uniform black-height and strict red-child separation.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(log n)` |
| **Space Complexity** | `O(n)` |

## Mathematical & Safety Invariants

- root is always BLACK
- no RED node ever has a RED child
- all root-to-leaf sentinel paths share identical black-height

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
