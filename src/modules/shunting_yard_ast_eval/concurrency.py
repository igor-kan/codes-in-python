from concurrent.futures import ThreadPoolExecutor
from typing import List
from fast_path import compile_and_eval

def parallel_eval(exprs: List[str]) -> List[int]:
    with ThreadPoolExecutor(max_workers=2) as pool:
        return list(pool.map(compile_and_eval, exprs))
