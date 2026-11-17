# Hirschberg Linear-Space Sequence Alignment & Edit Script (`levenshtein_hirschberg_linear`)

> Category: **Sequence Alignment** | Language: **Python 3.11+**

## Overview

Computes exact optimal string alignment and Levenshtein edit distance in O(M+N) working memory using Hirschberg's divide-and-conquer midpoint DP split.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(M * N) time` |
| **Space Complexity** | `O(min(M, N)) linear DP working vector` |

## Mathematical & Safety Invariants

- Aligned edit script transforms string A into string B with minimal edit count.
- Distance agrees identically with full O(M*N) Levenshtein DP.

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
