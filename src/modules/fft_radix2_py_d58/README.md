# Cooley-Tukey Radix-2 Exact Complex FFT & IFFT (`fft_radix2_py_d58`)

> Category: **Signal Processing** | Language: **Python 3.11+**

## Overview

Computes pure-Python radix-2 recursive Discrete Fourier Transforms and conjugate-scaled Inverse DFT roundtrips cleanly.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N log N)` |
| **Space Complexity** | `O(N log N)` |

## Mathematical & Safety Invariants

- IDFT(DFT(x)) reconstructs original real sequence within 1e-9 tolerance.

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
