# Dijkstra Shunting-Yard Infix Compiler & Constant-Folding AST Evaluator (`shunting_yard_ast_eval`)

> Category: **Parsing & Compilers** | Language: **Python 3.11+**

## Overview

Parses integer arithmetic expressions with parentheses and binary precedence via Dijkstra's Shunting-Yard algorithm into RPN, lowers into an immutable AST, and folds constant expressions.

## Complexity Guarantees

| Metric | Asymptotic Bound |
| :--- | :--- |
| **Time Complexity** | `O(N) operator-precedence shunting + AST fold` |
| **Space Complexity** | `O(N)` |

## Mathematical & Safety Invariants

- RPN stack depth invariants catch malformed arity or unbalanced parens.
- AST constant fold matches Python reference arithmetic semantics.

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
