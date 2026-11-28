# Cuckoo Filter with Fingerprint Relocation (`cuckoo_filter_py_d61`)

> Category: **Probabilistic Sketches** | Language: **Python 3.11+**

## Overview

Stores compact 16-bit fingerprints in two candidate buckets per item and performs bounded cuckoo eviction so membership and deletion avoid retaining full keys.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(1) expected membership with a bounded kick budget` |
| **Space Complexity** | `O(capacity) buckets of fingerprints` |

## Mathematical & Safety Invariants

- Inserted items are always found until removed and removal keeps the resident count exact.

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
