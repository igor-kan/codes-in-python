# Efraimidis-Spirakis A-Res Weighted Reservoir Sampling Without Replacement (`reservoir_weighted_chao`)

> Category: **Randomized Sampling** | Language: **Python 3.11+**

## Overview

Draws weighted samples of size K without replacement in a single pass using Efraimidis-Spirakis priority keys U_i^(1/w_i) maintained in a size-K binary min-heap.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N log K) min-heap key U^(1/w) streaming sampling` |
| **Space Complexity** | `O(K)` |

## Mathematical & Safety Invariants

- Sample has exact cardinality K distinct indices.
- Elements with strictly positive weights appear without negative-weight errors.

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
