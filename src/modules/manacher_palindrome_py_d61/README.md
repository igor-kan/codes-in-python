# Manacher Linear-Time Longest Palindromic Span (`manacher_palindrome_py_d61`)

> Category: **String Algorithms** | Language: **Python 3.11+**

## Overview

Finds the longest palindromic substring in linear time by computing odd and even radii with the Manacher mirror bound rather than per-center re-expansion.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N) radius expansion with mirror reuse` |
| **Space Complexity** | `O(N) radius arrays` |

## Mathematical & Safety Invariants

- The reported span is a palindrome and no longer palindrome exists.

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
