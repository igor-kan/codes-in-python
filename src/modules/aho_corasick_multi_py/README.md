# Multi-Pattern Aho-Corasick Failure-Link Automaton (`aho_corasick_multi_py`)

> Category: **String Matching** | Language: **Python 3.11+**

## Overview

Compiles a dictionary of patterns into an Aho-Corasick trie with BFS suffix failure links to count all pattern occurrences in a single linear scan.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N + sum(|P|)) BFS suffix-failure automaton scan` |
| **Space Complexity** | `O(Sigma * sum(|P|))` |

## Mathematical & Safety Invariants

- Total match count equals exact sum of occurrences across all patterns.

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
