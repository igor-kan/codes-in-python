from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def dinic_max_flow(n: int, s: int, t: int, edges: List[Tuple[int, int, int]]) -> int:
    adj: List[List[FlowEdge]] = [[] for _ in range(n)]
    for u, v, c in edges:
        adj[u].append(FlowEdge(v, len(adj[v]), c))
        adj[v].append(FlowEdge(u, len(adj[u]) - 1, 0))
    flow = 0
    while True:
        level = [-1] * n
        level[s] = 0
        q = [s]
        for u in q:
            for e in adj[u]:
                if e.cap > 0 and level[e.to] < 0:
                    level[e.to] = level[u] + 1
                    q.append(e.to)
        if level[t] < 0:
            break
        ptr = [0] * n
        def dfs(u: int, pushed: int) -> int:
            if pushed == 0 or u == t:
                return pushed
            while ptr[u] < len(adj[u]):
                e = adj[u][ptr[u]]
                if level[e.to] == level[u] + 1 and e.cap > 0:
                    tr = dfs(e.to, min(pushed, e.cap))
                    if tr > 0:
                        e.cap -= tr
                        adj[e.to][e.rev].cap += tr
                        return tr
                ptr[u] += 1
            return 0
        while True:
            p = dfs(s, 10**18)
            if p == 0:
                break
            flow += p
    return flow
