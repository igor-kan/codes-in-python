from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def johnson_apsp(n: int, edges: List[Tuple[int, int, int]]) -> DistanceMatrix:
    INF = 10**18
    h = [0] * n
    for _ in range(n):
        chg = False
        for u, v, w in edges:
            if h[u] + w < h[v]:
                h[v] = h[u] + w
                chg = True
        if not chg:
            break
    adj: List[List[Tuple[int, int]]] = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w + h[u] - h[v]))
    mat = [[INF] * n for _ in range(n)]
    for s in range(n):
        d = [INF] * n
        d[s] = 0
        pq: List[Tuple[int, int]] = [(0, s)]
        while pq:
            du, u = heapq.heappop(pq)
            if du > d[u]:
                continue
            for v, w in adj[u]:
                if du + w < d[v]:
                    d[v] = du + w
                    heapq.heappush(pq, (d[v], v))
        for v in range(n):
            if d[v] < INF:
                mat[s][v] = d[v] - h[s] + h[v]
    return DistanceMatrix(mat)
