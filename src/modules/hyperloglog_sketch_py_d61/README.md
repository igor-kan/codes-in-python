# HyperLogLog Log-Bucketed Cardinality Estimator (`hyperloglog_sketch_py_d61`)

> Category: **Probabilistic Sketches** | Language: **Python 3.11+**

## Overview

Estimates distinct-item cardinality with stochastic averaging of leading-zero ranks over 2^p registers plus linear-counting correction for small ranges.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(1) register update and O(registers) harmonic estimate` |
| **Space Complexity** | `O(2^p) registers` |

## Mathematical & Safety Invariants

- Merging sketch registers by pointwise maximum matches the estimate of the union stream.

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
