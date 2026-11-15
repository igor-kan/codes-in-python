# Floyd & Brent Functional Cycle Detector (`floyd_cycle_rho`)

> Category: **Graph / Number Theory** | Language: **Python 3.11+**

## Overview

Constant-space tortoise-and-hare plus Brent power-of-two functional graph cycle detector reporting exact tail length mu and period lambda.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(mu + lambda)` |
| **Space Complexity** | `O(1)` |

## Mathematical & Safety Invariants

- state[mu + lambda] == state[mu]
- mu >= 0 and lambda >= 1
- Floyd and Brent algorithms agree strictly on (mu, lambda, entry)

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
