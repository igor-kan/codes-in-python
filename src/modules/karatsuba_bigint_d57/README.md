# Divide-and-Conquer Karatsuba Fast Polynomial/Int Multiply (`karatsuba_bigint_d57`)

> Category: **Fast Algebra** | Language: **Python 3.11+**

## Overview

Splits large non-negative integers at base 10^k midpoints to reduce 4 recursive half-products to 3 via Gauss cross-term identity.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N^1.585)` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- Karatsuba product strictly matches built-in exact arbitrary-precision integer multiplication.

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
