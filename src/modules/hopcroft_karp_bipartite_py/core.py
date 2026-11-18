from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def hopcroft_karp(n_left: int, n_right: int, edges: List[Tuple[int, int]]) -> BipMatch:
    adj: List[List[int]] = [[] for _ in range(n_left)]
    for u, v in edges:
        adj[u].append(v)
    pair_u = [-1] * n_left
    pair_v = [-1] * n_right
    dist = [0] * n_left
    INF = 10**9
    def bfs() -> bool:
        q: List[int] = []
        for u in range(n_left):
            if pair_u[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        found = False
        for u in q:
            for v in adj[u]:
                u2 = pair_v[v]
                if u2 == -1:
                    found = True
                elif dist[u2] == INF:
                    dist[u2] = dist[u] + 1
                    q.append(u2)
        return found
    def dfs(u: int) -> bool:
        for v in adj[u]:
            u2 = pair_v[v]
            if u2 == -1 or (dist[u2] == dist[u] + 1 and dfs(u2)):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = INF
        return False
    size = 0
    while bfs():
        for u in range(n_left):
            if pair_u[u] == -1 and dfs(u):
                size += 1
    return BipMatch(size, pair_u)
