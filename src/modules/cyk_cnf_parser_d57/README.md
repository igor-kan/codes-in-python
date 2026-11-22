# CYK Bottom-Up Chomsky Normal Form Chart Recognizer (`cyk_cnf_parser_d57`)

> Category: **Formal Languages** | Language: **Python 3.11+**

## Overview

Builds bottom-up triangular CYK parse tables over CNF binary and terminal productions to decide context-free string acceptance cleanly.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(|w|^3 * |G|)` |
| **Space Complexity** | `O(|w|^2 * |V|)` |

## Mathematical & Safety Invariants

- Accepts valid nested CNF derivations and rejects unbalanced inputs.

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
