from typing import List, Optional, Sequence, Tuple
from models import PageRankResult
from validation import validate_pagerank_inputs


class SparsePageRank:
    def compute(
        self,
        n: int,
        edges: Sequence[Tuple[int, int]],
        damping: float = 0.85,
        tol: float = 1e-10,
        max_iter: int = 200,
        personalization: Optional[Sequence[float]] = None,
    ) -> PageRankResult:
        pers = validate_pagerank_inputs(n, edges, damping, tol, personalization)
        adj: List[List[int]] = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
        out_deg = [len(adj[u]) for u in range(n)]
        dangling = [u for u in range(n) if out_deg[u] == 0]

        r = list(pers)
        l1 = 1.0
        iters = 0
        for it in range(1, max_iter + 1):
            iters = it
            dang_mass = sum(r[u] for u in dangling)
            nxt = [(1.0 - damping + damping * dang_mass) * pers[v] for v in range(n)]
            for u in range(n):
                deg = out_deg[u]
                if deg > 0:
                    share = damping * r[u] / deg
                    for v in adj[u]:
                        nxt[v] += share
            l1 = sum(abs(nxt[v] - r[v]) for v in range(n))
            r = nxt
            if l1 <= tol:
                break
        return PageRankResult(tuple(r), iters, l1)
