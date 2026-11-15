from collections import deque
from typing import List, Sequence
from models import DirectedCapEdge


def scaling_edmonds_karp(n: int, edges: Sequence[DirectedCapEdge], source: int, sink: int) -> int:
    adj: List[List[List[int]]] = [[] for _ in range(n)]
    max_cap = 0
    for e in edges:
        max_cap = max(max_cap, e.cap)
        adj[e.u].append([e.v, e.cap, len(adj[e.v])])
        adj[e.v].append([e.u, 0, len(adj[e.u]) - 1])
    delta = 1
    while (delta << 1) <= max_cap:
        delta <<= 1
    total = 0
    while delta >= 1:
        while True:
            parent_v = [-1] * n
            parent_e = [-1] * n
            parent_v[source] = source
            q = deque([source])
            while q and parent_v[sink] == -1:
                u = q.popleft()
                for idx, (v, cap, _) in enumerate(adj[u]):
                    if cap >= delta and parent_v[v] == -1:
                        parent_v[v] = u
                        parent_e[v] = idx
                        q.append(v)
            if parent_v[sink] == -1:
                break
            aug = 1 << 60
            cur = sink
            while cur != source:
                p = parent_v[cur]
                eidx = parent_e[cur]
                aug = min(aug, adj[p][eidx][1])
                cur = p
            cur = sink
            while cur != source:
                p = parent_v[cur]
                eidx = parent_e[cur]
                edge = adj[p][eidx]
                edge[1] -= aug
                adj[cur][edge[2]][1] += aug
                cur = p
            total += aug
        delta >>= 1
    return total
