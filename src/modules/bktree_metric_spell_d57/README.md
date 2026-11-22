# Burkhard-Keller Discrete Metric Tree Fuzzy Dictionary (`bktree_metric_spell_d57`)

> Category: **Metric Trees** | Language: **Python 3.11+**

## Overview

Organizes lexicon strings by integer Levenshtein metric distances to enforce triangle-inequality pruning [d - rad, d + rad] during fuzzy matching.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(log N) typical discrete edit radius pruning` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- Returned candidate words match exhaustive radius-R filter identically.

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
