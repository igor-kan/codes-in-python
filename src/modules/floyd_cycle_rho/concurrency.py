from concurrent.futures import ThreadPoolExecutor
from typing import Callable, List, Sequence
from core import FloydCycleDetector
from models import CycleSignature


def batch_detect_cycles(
    step_fn: Callable[[int], int], seeds: Sequence[int], workers: int = 2
) -> List[CycleSignature[int]]:
    det = FloydCycleDetector()
    with ThreadPoolExecutor(max_workers=workers) as pool:
        return list(pool.map(lambda x0: det.detect(step_fn, x0), seeds))
