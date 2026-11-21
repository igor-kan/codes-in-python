from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def earley_accepts(grammar: Dict[str, List[Tuple[str, ...]]], start_sym: str, tokens: List[str]) -> bool:
    n = len(tokens)
    chart: List[List[Tuple[str, Tuple[str, ...], int, int]]] = [[] for _ in range(n + 1)]
    seen = [set() for _ in range(n + 1)]

    def add_state(pos: int, state: Tuple[str, Tuple[str, ...], int, int]) -> None:
        if state not in seen[pos]:
            seen[pos].add(state)
            chart[pos].append(state)

    for prod in grammar.get(start_sym, []):
        add_state(0, (start_sym, prod, 0, 0))
    for i in range(n + 1):
        idx = 0
        while idx < len(chart[i]):
            lhs, rhs, dot, origin = chart[i][idx]
            idx += 1
            if dot < len(rhs):
                sym = rhs[dot]
                if sym in grammar:
                    for prod in grammar[sym]:
                        add_state(i, (sym, prod, 0, i))
                elif i < n and tokens[i] == sym:
                    add_state(i + 1, (lhs, rhs, dot + 1, origin))
            else:
                for p_lhs, p_rhs, p_dot, p_orig in chart[origin]:
                    if p_dot < len(p_rhs) and p_rhs[p_dot] == lhs:
                        add_state(i, (p_lhs, p_rhs, p_dot + 1, p_orig))
    return any(lhs == start_sym and dot == len(rhs) and origin == 0 for lhs, rhs, dot, origin in chart[n])
