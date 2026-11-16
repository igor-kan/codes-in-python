from typing import List, Sequence, Set, Tuple
from models import SccResult
from validation import validate_digraph


class IterativeTarjanSCC:
    def decompose(self, n: int, edges: Sequence[Tuple[int, int]]) -> SccResult:
        validate_digraph(n, edges)
        adj: List[List[int]] = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)

        disc = [-1] * n
        low = [0] * n
        on_stack = [False] * n
        tarjan_stack: List[int] = []
        call_stack: List[Tuple[int, int]] = []
        timer = 0
        comp_id = [-1] * n
        comps: List[Tuple[int, ...]] = []

        for root in range(n):
            if disc[root] != -1:
                continue
            disc[root] = low[root] = timer
            timer += 1
            tarjan_stack.append(root)
            on_stack[root] = True
            call_stack.append((root, 0))

            while call_stack:
                u, idx = call_stack[-1]
                if idx < len(adj[u]):
                    v = adj[u][idx]
                    call_stack[-1] = (u, idx + 1)
                    if disc[v] == -1:
                        disc[v] = low[v] = timer
                        timer += 1
                        tarjan_stack.append(v)
                        on_stack[v] = True
                        call_stack.append((v, 0))
                    elif on_stack[v]:
                        if disc[v] < low[u]:
                            low[u] = disc[v]
                else:
                    call_stack.pop()
                    if call_stack:
                        p = call_stack[-1][0]
                        if low[u] < low[p]:
                            low[p] = low[u]
                    if low[u] == disc[u]:
                        cid = len(comps)
                        members: List[int] = []
                        while True:
                            w = tarjan_stack.pop()
                            on_stack[w] = False
                            comp_id[w] = cid
                            members.append(w)
                            if w == u:
                                break
                        members.sort()
                        comps.append(tuple(members))

        dag_set: Set[Tuple[int, int]] = set()
        for u, v in edges:
            cu, cv = comp_id[u], comp_id[v]
            if cu != cv:
                dag_set.add((cu, cv))
        return SccResult(tuple(comp_id), tuple(comps), tuple(sorted(dag_set)))
