from collections import deque
from typing import List, Sequence
from exceptions import FlowDimensionError, FlowDomainError
from models import DirectedCapEdge, MaxFlowReport


class DinicMaxFlowSolver:
    def solve(self, n: int, edges: Sequence[DirectedCapEdge], source: int, sink: int) -> MaxFlowReport:
        if source == sink:
            raise FlowDomainError("source and sink must differ")
        adj: List[List[List[int]]] = [[] for _ in range(n)]
        for e in edges:
            fwd = [e.v, e.cap, len(adj[e.v])]
            rev = [e.u, 0, len(adj[e.u])]
            adj[e.u].append(fwd)
            adj[e.v].append(rev)

        def bfs(level: List[int]) -> bool:
            for i in range(n):
                level[i] = -1
            level[source] = 0
            q = deque([source])
            while q:
                u = q.popleft()
                for v, cap, _ in adj[u]:
                    if cap > 0 and level[v] < 0:
                        level[v] = level[u] + 1
                        q.append(v)
            return level[sink] >= 0

        def dfs(u: int, pushed: int, level: List[int], ptr: List[int]) -> int:
            if pushed == 0 or u == sink:
                return pushed
            while ptr[u] < len(adj[u]):
                edge = adj[u][ptr[u]]
                v, cap, rev_idx = edge
                if cap > 0 and level[v] == level[u] + 1:
                    tr = dfs(v, min(pushed, cap), level, ptr)
                    if tr > 0:
                        edge[1] -= tr
                        adj[v][rev_idx][1] += tr
                        return tr
                ptr[u] += 1
            return 0

        total = 0
        level = [-1] * n
        while bfs(level):
            ptr = [0] * n
            while True:
                pushed = dfs(source, 1 << 60, level, ptr)
                if pushed == 0:
                    break
                total += pushed

        reachable: set[int] = {source}
        q = deque([source])
        while q:
            u = q.popleft()
            for v, cap, _ in adj[u]:
                if cap > 0 and v not in reachable:
                    reachable.add(v)
                    q.append(v)
        return MaxFlowReport(max_flow=total, min_cut_source_side=tuple(sorted(reachable)))
