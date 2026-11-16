from concurrent.futures import ThreadPoolExecutor
from typing import List, Sequence, Tuple
from core import BranchAndBoundKnapsack
from models import KnapsackItem, KnapsackPlan


def parallel_solve_instances(instances: Sequence[Tuple[Sequence[KnapsackItem], int]]) -> List[KnapsackPlan]:
    solver = BranchAndBoundKnapsack()
    with ThreadPoolExecutor(max_workers=4) as pool:
        futs = [pool.submit(solver.solve, items, cap) for items, cap in instances]
        return [f.result() for f in futs]
