from concurrent.futures import ThreadPoolExecutor
from typing import List
from models import JobInterval
from core import solve_weighted_intervals

def parallel_best_weights(batches: List[List[JobInterval]]) -> List[int]:
    with ThreadPoolExecutor(max_workers=2) as pool:
        return list(pool.map(lambda b: solve_weighted_intervals(b)[0], batches))
