from concurrent.futures import ThreadPoolExecutor
from typing import List, Sequence, Tuple
from core import SparsePageRank
from models import PageRankResult


def batch_pagerank(tasks: Sequence[Tuple[int, Sequence[Tuple[int, int]]]]) -> List[PageRankResult]:
    eng = SparsePageRank()
    with ThreadPoolExecutor(max_workers=4) as pool:
        return list(pool.map(lambda t: eng.compute(t[0], t[1]), tasks))
