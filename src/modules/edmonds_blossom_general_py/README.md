# Edmonds Blossom Odd-Cycle Contracting General Graph Matcher (`edmonds_blossom_general_py`)

> Category: **Graph Matching** | Language: **Python 3.11+**

## Overview

Computes maximum cardinality matching on general graphs by contracting odd cycles around their lowest common ancestor in the alternating forest.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(V^3) BFS augmenting tree with blossom LCA contraction` |
| **Space Complexity** | `O(V + E)` |

## Mathematical & Safety Invariants

- Contracts odd cycles cleanly and finds maximum matching size.

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
