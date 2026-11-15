from concurrent.futures import ThreadPoolExecutor
from typing import List, Optional, Sequence
from core import RedBlackOrderedMap


def parallel_lookups(tree: RedBlackOrderedMap, keys: Sequence[int]) -> List[Optional[int]]:
    with ThreadPoolExecutor(max_workers=2) as pool:
        return list(pool.map(tree.get, keys))
