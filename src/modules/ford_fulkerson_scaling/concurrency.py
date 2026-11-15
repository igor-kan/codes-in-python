from concurrent.futures import ThreadPoolExecutor
from typing import List, Sequence, Tuple
from core import DinicMaxFlowSolver
from models import DirectedCapEdge


def solve_demands_parallel(
    n: int, edges: Sequence[DirectedCapEdge], st_pairs: Sequence[Tuple[int, int]], workers: int = 2
) -> List[int]:
    solver = DinicMaxFlowSolver()
    with ThreadPoolExecutor(max_workers=workers) as pool:
        return list(pool.map(lambda st: solver.solve(n, edges, st[0], st[1]).max_flow, st_pairs))
