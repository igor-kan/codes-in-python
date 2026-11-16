from concurrent.futures import ThreadPoolExecutor
from typing import List, Sequence
from core import KdTreeIndex
from models import NeighborHit


def batch_knn(idx: KdTreeIndex, queries: Sequence[Sequence[float]], k: int) -> List[List[NeighborHit]]:
    with ThreadPoolExecutor(max_workers=4) as pool:
        return list(pool.map(lambda q: idx.k_nearest(q, k), queries))
