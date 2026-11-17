# Misra-Gries / Generalized Boyer-Moore K-Majority Streaming Tracker (`boyer_moore_majority_k`)

> Category: **Streaming Algorithms** | Language: **Python 3.11+**

## Overview

Extracts all stream elements appearing strictly more than floor(N / K) times using at most K-1 Misra-Gries paired counters and exact verification pass.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N * K) two-pass exact heavy-hitter extractor` |
| **Space Complexity** | `O(K)` |

## Mathematical & Safety Invariants

- Every emitted candidate occurs strictly more than N // K times in exact histogram.
- No true (> N // K) heavy hitter is ever missed.

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
