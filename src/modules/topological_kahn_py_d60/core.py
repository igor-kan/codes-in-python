from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def kahn_lex_topo(n: int, edges: List[DagEdge]) -> List[int]:
    if n <= 0:
        raise ValidationError("n must be > 0")
    adj: List[List[int]] = [[] for _ in range(n)]
    indeg = [0] * n
    for e in edges:
        adj[e.u].append(e.v)
        indeg[e.v] += 1
    hq = [i for i in range(n) if indeg[i] == 0]
    heapq.heapify(hq)
    order: List[int] = []
    while hq:
        u = heapq.heappop(hq)
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                heapq.heappush(hq, v)
    if len(order) != n:
        raise ValidationError("cycle detected in directed graph")
    return order


def dag_longest_path(n: int, edges: List[DagEdge]) -> int:
    order = kahn_lex_topo(n, edges)
    adj: List[List[Tuple[int, int]]] = [[] for _ in range(n)]
    for e in edges:
        adj[e.u].append((e.v, e.weight))
    dp = [0] * n
    for u in order:
        for v, w in adj[u]:
            if dp[u] + w > dp[v]:
                dp[v] = dp[u] + w
    return max(dp)
