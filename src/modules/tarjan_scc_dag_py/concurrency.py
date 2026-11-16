from concurrent.futures import ThreadPoolExecutor
from typing import List, Sequence, Tuple
from core import IterativeTarjanSCC
from models import SccResult


def batch_scc(graphs: Sequence[Tuple[int, Sequence[Tuple[int, int]]]]) -> List[SccResult]:
    eng = IterativeTarjanSCC()
    with ThreadPoolExecutor(max_workers=4) as pool:
        return list(pool.map(lambda g: eng.decompose(g[0], g[1]), graphs))
