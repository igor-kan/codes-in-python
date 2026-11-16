# Static 3-Wise XOR Peeling Filter (Zero False Negatives) (`bloomier_perfect_filter`)

> Category: **Probabilistic Membership Filters** | Language: **Python 3.11+**

## Overview

Builds a Graf-Lemire style static XOR Filter over finite integer sets by iteratively peeling degree-1 vertices from a 3-regular partitioned hypergraph and assigning 16-bit fingerprints backwards so member lookups equal f0 ^ f1 ^ f2.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N) graph-peeling construction, O(1) 3-probe lookup` |
| **Space Complexity** | `~1.23 * N * 16-bit fingerprints` |

## Mathematical & Safety Invariants

- Every key present in build input returns contains(k) == True with zero false negatives.
- Random unseen probe false-positive rate hovers near 2^-16 (~0.0015%).

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
