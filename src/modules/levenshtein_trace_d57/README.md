# Levenshtein Edit Distance With Op-Trace Reconstruction (`levenshtein_trace_d57`)

> Category: **Sequence Alignment** | Language: **Python 3.11+**

## Overview

Computes full DP edit matrix and backtracks exact ('M', 'I', 'D', 'R') edit-script operations yielding identical Levenshtein distance.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(M * N)` |
| **Space Complexity** | `O(M * N)` |

## Mathematical & Safety Invariants

- Number of non-'M' operations in the backtracked script equals exact DP edit cost.

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
