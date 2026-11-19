# Rubinchik-Shur Eertree Distinct Palindrome Substring Automaton (`eertree_palin_tree_py`)

> Category: **String Automata** | Language: **Python 3.11+**

## Overview

Maintains two palindrome roots (-1 and 0) and suffix links to enumerate every distinct palindromic substring in linear time.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N) online palindrome discovery + suffix-link traversal` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- State count - 2 equals exact count of distinct non-empty palindromes.

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
