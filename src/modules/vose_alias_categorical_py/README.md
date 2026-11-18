# Vose O(1) Alias Table Discrete Categorical Sampler (`vose_alias_categorical_py`)

> Category: **Randomized Algorithms** | Language: **Python 3.11+**

## Overview

Constructs Vose's O(1) Alias Table from arbitrary unnormalized weights using small/large worklists.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N) table construction + O(1) bucket draw` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- Every bucket mixes at most two outcomes and preserves exact categorical probabilities.

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
