from typing import List, Sequence, Tuple


def reachable_pair(n: int, edges: Sequence[Tuple[int, int]], src: int, dst: int) -> bool:
    adj: List[List[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
    seen = [False] * n
    q = [src]
    seen[src] = True
    while q:
        u = q.pop()
        if u == dst:
            return True
        for v in adj[u]:
            if not seen[v]:
                seen[v] = True
                q.append(v)
    return False
