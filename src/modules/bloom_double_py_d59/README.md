# Arbitrary-Precision Bitwise Double-Hash Bloom Filter (`bloom_double_py_d59`)

> Category: **Probabilistic Sketches** | Language: **Python 3.11+**

## Overview

Packs compact Bloom filter membership bits inside a single Python int mask using Kirsch-Mitzenmacher derived bit indices cleanly.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(K) bit checks` |
| **Space Complexity** | `O(M bits)` |

## Mathematical & Safety Invariants

- Every added member strictly returns True with zero false negatives.

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
