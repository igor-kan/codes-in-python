# Dangling-Node-Safe Sparse Personalized PageRank Power Iterator (`pagerank_power_iter`)

> Category: **Graph Centrality & Linear Algebra** | Language: **Python 3.11+**

## Overview

Computes stationary PageRank vectors via damping alpha, stochastic dangling-sink probability redistribution, and personalization vectors until L1 delta converges below tolerance.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(Iterations * (V + E))` |
| **Space Complexity** | `O(V + E)` |

## Mathematical & Safety Invariants

- Stationary rank vector sums strictly to 1.0 within 1e-10 and stays non-negative.
- Symmetric regular cycle/complete graphs assign identical stationary mass 1/N to every vertex.

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
