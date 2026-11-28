from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

from collections import deque


def min_cost_flow(n: int, s: int, t: int, edges: List[Tuple[int, int, int, int]]) -> McfResult:
    if n <= 0 or not (0 <= s < n) or not (0 <= t < n):
        raise ValidationError("node indices must lie inside [0, n)")
    if s == t:
        raise ValidationError("source and sink must differ")
    adj: List[List[McfEdge]] = [[] for _ in range(n)]
    for u, v, cap, cost in edges:
        if cap < 0:
            raise ValidationError("edge capacity must be non-negative")
        adj[u].append(McfEdge(v, len(adj[v]), cap, cost))
        adj[v].append(McfEdge(u, len(adj[u]) - 1, 0, -cost))
    total_flow = 0
    total_cost = 0
    inf = 10 ** 18
    while True:
        dist = [inf] * n
        in_queue = [False] * n
        prev_node = [-1] * n
        prev_edge = [-1] * n
        dist[s] = 0
        queue = deque([s])
        in_queue[s] = True
        while queue:
            u = queue.popleft()
            in_queue[u] = False
            for i, e in enumerate(adj[u]):
                if e.cap > 0 and dist[u] + e.cost < dist[e.to]:
                    dist[e.to] = dist[u] + e.cost
                    prev_node[e.to] = u
                    prev_edge[e.to] = i
                    if not in_queue[e.to]:
                        in_queue[e.to] = True
                        queue.append(e.to)
        if dist[t] == inf:
            break
        pushed = inf
        v = t
        while v != s:
            pushed = min(pushed, adj[prev_node[v]][prev_edge[v]].cap)
            v = prev_node[v]
        v = t
        while v != s:
            e = adj[prev_node[v]][prev_edge[v]]
            e.cap -= pushed
            adj[v][e.rev].cap += pushed
            v = prev_node[v]
        total_flow += pushed
        total_cost += pushed * dist[t]
    return McfResult(flow=total_flow, cost=total_cost)
