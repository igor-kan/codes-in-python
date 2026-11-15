from concurrent.futures import ThreadPoolExecutor
from typing import List, Sequence
from core import BlandSimplexSolver
from models import LinearProgram, SimplexSolution


def solve_lp_portfolio(programs: Sequence[LinearProgram]) -> List[SimplexSolution]:
    solver = BlandSimplexSolver()
    with ThreadPoolExecutor(max_workers=2) as pool:
        return list(pool.map(solver.maximize, programs))
