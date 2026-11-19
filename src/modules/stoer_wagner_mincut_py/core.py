from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def stoer_wagner_mincut(n: int, adj: List[List[int]]) -> CutSummary:
    w = [row[:] for row in adj]
    vtx = list(range(n))
    best = 10**18
    phases = 0
    for m in range(n, 1, -1):
        wt = [0] * m
        used = [False] * m
        prev = -1
        last = -1
        for _ in range(m):
            sel = max((i for i in range(m) if not used[i]), key=lambda i: wt[i])
            used[sel] = True
            prev, last = last, sel
            for i in range(m):
                if not used[i]:
                    wt[i] += w[vtx[sel]][vtx[i]]
        best = min(best, wt[last])
        phases += 1
        u, v = vtx[prev], vtx[last]
        for i in range(m):
            k = vtx[i]
            if k != u and k != v:
                w[u][k] += w[v][k]
                w[k][u] += w[k][v]
        vtx[last] = vtx[m - 1]
    return CutSummary(best, phases)
