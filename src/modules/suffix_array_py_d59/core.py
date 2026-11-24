from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def suffix_array_and_lcp(s: str) -> Tuple[List[int], List[int], int]:
    n = len(s)
    if n == 0:
        return [], [], 0
    sa = list(range(n))
    rk = [ord(c) for c in s]
    k = 1
    while k < n:
        sa.sort(key=lambda i: (rk[i], rk[i + k] if i + k < n else -1))
        tmp = [0] * n
        for i in range(1, n):
            a, b = sa[i - 1], sa[i]
            pa = (rk[a], rk[a + k] if a + k < n else -1)
            pb = (rk[b], rk[b + k] if b + k < n else -1)
            tmp[b] = tmp[a] + (1 if pa != pb else 0)
        rk = tmp
        if rk[sa[-1]] == n - 1:
            break
        k <<= 1
    lcp = [0] * n
    rank_of = [0] * n
    for i, pos in enumerate(sa):
        rank_of[pos] = i
    h = 0
    for i in range(n):
        if rank_of[i] == n - 1:
            h = 0
            continue
        j = sa[rank_of[i] + 1]
        while i + h < n and j + h < n and s[i + h] == s[j + h]:
            h += 1
        lcp[rank_of[i]] = h
        if h > 0:
            h -= 1
    distinct = n * (n + 1) // 2 - sum(lcp)
    return sa, lcp, distinct
