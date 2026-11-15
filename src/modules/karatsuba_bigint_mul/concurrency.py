from concurrent.futures import ThreadPoolExecutor
from typing import List, Sequence, Tuple
from core import KaratsubaMultiplier
from models import LimbBigInt


def batch_multiply(pairs: Sequence[Tuple[LimbBigInt, LimbBigInt]]) -> List[LimbBigInt]:
    mul = KaratsubaMultiplier()
    with ThreadPoolExecutor(max_workers=2) as pool:
        return list(pool.map(lambda ab: mul.multiply(ab[0], ab[1]), pairs))
