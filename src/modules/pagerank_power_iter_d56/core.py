from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def pagerank_scores(n: int, edges: List[Tuple[int, int]], damping: float = 0.85, iters: int = 50) -> List[float]:
    if n <= 0:
        raise ValidationError("n must be positive")
    out_adj: List[List[int]] = [[] for _ in range(n)]
    for u, v in edges:
        out_adj[u].append(v)
    rank = [1.0 / n] * n
    base = (1.0 - damping) / n
    for _ in range(iters):
        nxt = [base] * n
        dangling_sum = sum(rank[u] for u in range(n) if not out_adj[u])
        dang_share = damping * dangling_sum / n
        for i in range(n):
            nxt[i] += dang_share
        for u in range(n):
            deg = len(out_adj[u])
            if deg > 0:
                share = damping * rank[u] / deg
                for v in out_adj[u]:
                    nxt[v] += share
        rank = nxt
    return rank
