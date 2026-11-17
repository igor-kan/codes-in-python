from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple
from core import analyze_dag

def parallel_batch_analyze(jobs: List[Tuple[int, List[Tuple[int, int]], int]]) -> List[int]:
    with ThreadPoolExecutor(max_workers=2) as pool:
        futs = [pool.submit(lambda j=j: analyze_dag(j[0], j[1], j[2]).path_counts[-1]) for j in jobs]
        return [f.result() for f in futs]
