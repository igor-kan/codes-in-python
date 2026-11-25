from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def _lev_row(a: str, b: str) -> List[int]:
    prev = list(range(len(b) + 1))
    for ca in a:
        curr = [prev[0] + 1]
        for j, cb in enumerate(b):
            cost = 0 if ca == cb else 1
            curr.append(min(curr[-1] + 1, prev[j + 1] + 1, prev[j] + cost))
        prev = curr
    return prev


def hirschberg_align(a: str, b: str) -> List[AlignStep]:
    n, m = len(a), len(b)
    if n == 0:
        return [AlignStep("ins", "-", ch) for ch in b]
    if m == 0:
        return [AlignStep("del", ch, "-") for ch in a]
    if n == 1:
        if a[0] in b:
            pos = b.index(a[0])
            return ([AlignStep("ins", "-", b[j]) for j in range(pos)]
                    + [AlignStep("eq", a[0], a[0])]
                    + [AlignStep("ins", "-", b[j]) for j in range(pos + 1, m)])
        return [AlignStep("sub", a[0], b[0])] + [AlignStep("ins", "-", b[j]) for j in range(1, m)]
    mid = n // 2
    fwd = _lev_row(a[:mid], b)
    rev = _lev_row(a[mid:][::-1], b[::-1])[::-1]
    split_j = min(range(m + 1), key=lambda j: fwd[j] + rev[j])
    return hirschberg_align(a[:mid], b[:split_j]) + hirschberg_align(a[mid:], b[split_j:])


def edit_cost(steps: List[AlignStep]) -> int:
    return sum(0 if s.op == "eq" else 1 for s in steps)
