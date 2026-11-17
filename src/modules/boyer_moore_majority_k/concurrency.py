from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List
from core import misra_gries_heavy

def parallel_heavy_hitters(streams: List[List[int]], k: int) -> List[Dict[int, int]]:
    with ThreadPoolExecutor(max_workers=2) as pool:
        return list(pool.map(lambda s: misra_gries_heavy(s, k).verified_counts, streams))
