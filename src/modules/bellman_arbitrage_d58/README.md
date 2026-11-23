# Log-Transform FX Arbitrage Negative-Cycle Detector (`bellman_arbitrage_d58`)

> Category: **Computational Finance Graphs** | Language: **Python 3.11+**

## Overview

Converts currency cross-exchange rate matrices via -log(rate) into additive edge weights and runs Bellman-Ford to flag positive risk-free arbitrage loops.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N^3)` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- Self-consistent cross-rates satisfy r_ij * r_jk * r_ki == 1 with no arbitrage detected.

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
