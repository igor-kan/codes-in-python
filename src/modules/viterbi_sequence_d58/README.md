# Log-Space Discrete Viterbi Sequence Alignment Decoder (`viterbi_sequence_d58`)

> Category: **Sequence Decoding** | Language: **Python 3.11+**

## Overview

Computes exact optimal hidden-state trajectories in log-space across stochastic Markov emissions without floating underflow.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(T * S^2)` |
| **Space Complexity** | `O(T * S)` |

## Mathematical & Safety Invariants

- Length of decoded path equals observation count identically.

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
