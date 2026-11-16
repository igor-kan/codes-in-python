from typing import Sequence, Tuple
from exceptions import TarjanSccDomainError
from fast_path import reachable_pair
from models import SccResult


def verify_scc_invariants(n: int, edges: Sequence[Tuple[int, int]], res: SccResult) -> None:
    if len(res.comp_ids) != n:
        raise TarjanSccDomainError("comp_ids size != n")
    for cu, cv in res.condensation_edges:
        if cu <= cv:
            raise TarjanSccDomainError("condensation edge violates reverse Tarjan DAG topological order")
    if n <= 20:
        for u in range(n):
            for v in range(u + 1, n):
                mutual = reachable_pair(n, edges, u, v) and reachable_pair(n, edges, v, u)
                if mutual != (res.comp_ids[u] == res.comp_ids[v]):
                    raise TarjanSccDomainError(f"mutual reachability oracle failed on ({u}, {v})")
