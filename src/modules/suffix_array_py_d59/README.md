# Prefix-Doubling Suffix Array & Kasai LCP Builder (`suffix_array_py_d59`)

> Category: **Suffix Indexing** | Language: **Python 3.11+**

## Overview

Constructs lexicographic suffix index permutations using doubling rank sorts followed by linear Kasai LCP array computation.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N log^2 N) SA + O(N) Kasai LCP` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- Distinct non-empty substring count strictly equals N*(N+1)//2 - sum(lcp).

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
