from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple
from core import align_hirschberg

def parallel_align(pairs: List[Tuple[str, str]]) -> List[int]:
    with ThreadPoolExecutor(max_workers=2) as pool:
        return list(pool.map(lambda p: align_hirschberg(p[0], p[1]).distance, pairs))
