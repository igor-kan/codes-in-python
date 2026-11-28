# Segmented Sieve of Eratosthenes Prime Enumerator (`segmented_sieve_py_d61`)

> Category: **Number Theory** | Language: **Python 3.11+**

## Overview

Enumerates all primes up to a limit by sieving consecutive fixed-size windows with base primes discovered up to the square root, keeping memory independent of the limit.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N log log N) total marking across fixed-size segments` |
| **Space Complexity** | `O(sqrt(N)) base primes plus one segment` |

## Mathematical & Safety Invariants

- Every reported value is prime and the count matches the prime counting function.

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
