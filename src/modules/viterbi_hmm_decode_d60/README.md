# Log-Domain Viterbi Hidden Markov Model State Sequence Decoder (`viterbi_hmm_decode_d60`)

> Category: **Probabilistic Models** | Language: **Python 3.11+**

## Overview

Computes the maximum a posteriori hidden state path over discrete emission sequences in numerically stable log-probability arithmetic.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(T * S^2) dynamic programming backtracking` |
| **Space Complexity** | `O(T * S)` |

## Mathematical & Safety Invariants

- Decoded state path realizes max joint log-likelihood across S^T paths.

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
