from concurrent.futures import ThreadPoolExecutor
from typing import List, Sequence
from core import Xor16Filter
from models import XorFilterTable


def parallel_build_shards(shards: Sequence[Sequence[int]]) -> List[XorFilterTable]:
    eng = Xor16Filter()
    with ThreadPoolExecutor(max_workers=4) as pool:
        return list(pool.map(eng.build, shards))
