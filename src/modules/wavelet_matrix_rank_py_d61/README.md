# Wavelet Matrix Range Rank and Quantile Index (`wavelet_matrix_rank_py_d61`)

> Category: **Succinct Data Structures** | Language: **Python 3.11+**

## Overview

Indexes a static integer sequence into a wavelet matrix so range rank counts and k-th smallest order statistics run in a number of steps proportional to the value bit width.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(B) rank/quantile queries after O(N * B) construction` |
| **Space Complexity** | `O(N * B) bit-prefix counters` |

## Mathematical & Safety Invariants

- Range ranks equal naive counts and quantiles equal sorted subrange indexing.

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
