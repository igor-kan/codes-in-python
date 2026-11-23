from concurrent.futures import ThreadPoolExecutor
from typing import List
from fast_path import fast_fold_ints

def parallel_fold_batches(batches: List[List[int]]) -> List[int]:
    with ThreadPoolExecutor(max_workers=2) as pool:
        return list(pool.map(fast_fold_ints, batches))
