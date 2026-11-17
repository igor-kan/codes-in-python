from concurrent.futures import ThreadPoolExecutor
from typing import Callable, List
from core import nelder_mead

def parallel_restarts(fn: Callable[[List[float]], float], starts: List[List[float]]) -> float:
    with ThreadPoolExecutor(max_workers=2) as pool:
        return min(r.fval for r in pool.map(lambda s: nelder_mead(fn, s, 800, 1e-10), starts))
