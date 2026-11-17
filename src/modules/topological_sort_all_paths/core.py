import heapq
from typing import List, Tuple
from models import DagSummary
from exceptions import DagSortValidationError


def analyze_dag(n: int, edges: List[Tuple[int, int]], src: int = 0) -> DagSummary:
    if n <= 0 or not (0 <= src < n):
        raise DagSortValidationError("invalid node count or source")
    adj: List[List[int]] = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        if not (0 <= u < n and 0 <= v < n):
            raise DagSortValidationError("edge endpoint out of bounds")
        adj[u].append(v)
        indeg[v] += 1
    pq = [i for i in range(n) if indeg[i] == 0]
    heapq.heapify(pq)
    order: List[int] = []
    while pq:
        u = heapq.heappop(pq)
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                heapq.heappush(pq, v)
    if len(order) != n:
        raise DagSortValidationError("directed cycle detected")
    dist = [0] * n
    ways = [0] * n
    ways[src] = 1
    for u in order:
        for v in adj[u]:
            if dist[u] + 1 > dist[v]:
                dist[v] = dist[u] + 1
            ways[v] += ways[u]
    return DagSummary(order=order, longest_dist=dist, path_counts=ways)
