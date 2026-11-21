# Optimal String Alignment Damerau-Levenshtein Distance (`damerau_levenshtein_osa_d56`)

> Category: **String Edit Metrics** | Language: **Python 3.11+**

## Overview

Computes Optimal String Alignment edit distance supporting substitution, insertion, deletion, and single adjacent character transpositions cleanly.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(M * N)` |
| **Space Complexity** | `O(M * N)` |

## Mathematical & Safety Invariants

- Distance is zero iff inputs match and satisfies symmetry d(a, b) == d(b, a).

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
