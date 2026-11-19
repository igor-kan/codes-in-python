# Linear-Time Suffix Automaton (SAM) Distinct Substring Counter (`suffix_automaton_dawg_py`)

> Category: **String Automata** | Language: **Python 3.11+**

## Overview

Constructs Blumer's minimal Suffix Automaton in O(N) time and computes both exact distinct substring multiplicity and longest common substring.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N) online SAM state extension + O(M) LCS match` |
| **Space Complexity** | `O(N) states` |

## Mathematical & Safety Invariants

- Distinct substrings equals exact cardinality of unique non-empty substrings.

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
