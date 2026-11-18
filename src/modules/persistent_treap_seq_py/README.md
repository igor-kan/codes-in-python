# Path-Copied Persistent Implicit Treap Sequence (`persistent_treap_seq_py`)

> Category: **Persistent Structures** | Language: **Python 3.11+**

## Overview

Maintains immutable sequence versions via functional treap split and merge that copy only root-to-split-path nodes.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(log N) functional split, merge, and range sum` |
| **Space Complexity** | `O(N + Q log N)` |

## Mathematical & Safety Invariants

- Earlier version roots preserve their exact elements and sums after updates.

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
