from concurrent.futures import ThreadPoolExecutor
from typing import List
from models import WeightedItem
from core import ares_sample

def parallel_trials(items: List[WeightedItem], k: int, seeds: List[int]) -> List[List[int]]:
    with ThreadPoolExecutor(max_workers=2) as pool:
        return list(pool.map(lambda s: ares_sample(items, k, s), seeds))
