# Iterative Bit-Reversal Radix-2 Cooley-Tukey FFT & IFFT (`spectral_fft_cooley`)

> Category: **Signal Processing & Numerical Transforms** | Language: **Python 3.11+**

## Overview

Implements iterative in-place bit-reversed Cooley-Tukey Fast Fourier Transform and normalized inverse FFT for power-of-two complex sequences verified against Parseval energy conservation and exact DFT.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N log N)` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- ifft(fft(x)) recovers original complex signal within 1e-10 L_inf error.
- Parseval identity holds: sum(|x_n|^2) == (1/N) * sum(|X_k|^2).

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
