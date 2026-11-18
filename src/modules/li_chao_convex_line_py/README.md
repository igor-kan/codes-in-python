# Dynamic Li Chao Segment Tree for Lower-Envelope Line Queries (`li_chao_convex_line_py`)

> Category: **Convex Hull Optimization** | Language: **Python 3.11+**

## Overview

Stores dominant affine lines y = m*x + b at segment midpoints over [0, X) to answer lower-envelope queries in O(log X) time.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(log X) line insertion and point minimum evaluation` |
| **Space Complexity** | `O(X)` |

## Mathematical & Safety Invariants

- Query at x returns exact min_i (m_i * x + b_i) across all inserted lines.

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
