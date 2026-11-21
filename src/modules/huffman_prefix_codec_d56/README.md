# Huffman Optimal Binary Prefix Tree Codec (`huffman_prefix_codec_d56`)

> Category: **Entropy Coding** | Language: **Python 3.11+**

## Overview

Builds minimum-redundancy binary prefix codes via min-heap symbol merging and decodes serialized bitstrings back into exact symbols.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(Sigma log Sigma + N)` |
| **Space Complexity** | `O(Sigma)` |

## Mathematical & Safety Invariants

- Weighted path length minimizes expected code bits and encode->decode is lossless.

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
