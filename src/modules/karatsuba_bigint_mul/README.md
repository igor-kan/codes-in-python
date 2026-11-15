# Karatsuba Arbitrary-Radix Limb Multiplier (`karatsuba_bigint_mul`)

> Category: **Algorithms / Arbitrary Precision** | Language: **Python 3.11+**

## Overview

Divide-and-conquer Karatsuba polynomial/limb multiplication over base-10^4 integer digits with carry normalization and native bigint oracle.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(n^1.585)` |
| **Space Complexity** | `O(n)` |

## Mathematical & Safety Invariants

- output limbs stay strictly canonical in [0, BASE) with no trailing leading zeros
- multiplication is commutative and matches native Python integer product
- zero-input annihilates cleanly to empty zero representation

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
