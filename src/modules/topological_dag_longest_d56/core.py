from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def dag_longest_path(n: int, edges: List[Tuple[int, int, int]]) -> Tuple[int, List[int]]:
    if n <= 0:
        raise ValidationError("n must be positive")
    adj: List[List[Tuple[int, int]]] = [[] for _ in range(n)]
    ind = [0] * n
    for u, v, w in edges:
        adj[u].append((v, w))
        ind[v] += 1
    q = [i for i in range(n) if ind[i] == 0]
    topo: List[int] = []
    head = 0
    while head < len(q):
        u = q[head]
        head += 1
        topo.append(u)
        for v, _ in adj[u]:
            ind[v] -= 1
            if ind[v] == 0:
                q.append(v)
    if len(topo) != n:
        raise ValidationError("cycle detected in DAG")
    dist = [0] * n
    for u in topo:
        for v, w in adj[u]:
            if dist[u] + w > dist[v]:
                dist[v] = dist[u] + w
    return max(dist), dist
