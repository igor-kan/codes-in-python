# Earley Context-Free Grammar Chart Recognizer (`earley_cfg_recogniser_d56`)

> Category: **Parsing Theory** | Language: **Python 3.11+**

## Overview

Parses arbitrary context-free grammars including left-recursive rules via predictor, scanner, and completer chart closure.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(|w|^3) general CFG, O(|w|) LR(k)` |
| **Space Complexity** | `O(|w|^2)` |

## Mathematical & Safety Invariants

- Recognizes balanced recursive grammar derivations and rejects malformed token strings.

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
