# Log-Space HMM Viterbi Decoder (`viterbi_hmm_decoder`)

> Category: **Probabilistic Graphical Models** | Language: **Python 3.11+**

## Overview

Numerically stable log-probability Viterbi MAP sequence decoder and Forward log-sum-exp marginal evaluator for discrete Hidden Markov Models.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(T * S^2)` |
| **Space Complexity** | `O(T * S)` |

## Mathematical & Safety Invariants

- every transition row and initial distribution sums to 1.0 within 1e-9
- decoded Viterbi path length equals observation sequence length T
- Viterbi path log-probability >= any exhaustive enumeration path log-prob

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
