from concurrent.futures import ThreadPoolExecutor
from typing import List, Sequence
from core import HungarianPotentialSolver
from models import AssignmentResult


def batch_solve_assignments(matrices: Sequence[Sequence[Sequence[float]]]) -> List[AssignmentResult]:
    solver = HungarianPotentialSolver()
    with ThreadPoolExecutor(max_workers=4) as pool:
        return list(pool.map(solver.solve_min_cost, matrices))
