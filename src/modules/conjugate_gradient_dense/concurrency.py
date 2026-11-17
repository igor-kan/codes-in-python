from concurrent.futures import ThreadPoolExecutor
from typing import List
from core import solve_pcg

def parallel_solve_rhs(a: List[List[float]], rhs_list: List[List[float]]) -> List[List[float]]:
    with ThreadPoolExecutor(max_workers=2) as pool:
        return list(pool.map(lambda b: solve_pcg(a, b).x, rhs_list))
