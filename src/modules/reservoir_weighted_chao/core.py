import heapq, math, random
from typing import Iterable, List, Tuple
from models import WeightedItem
from exceptions import WeightedSampleValidationError


def ares_sample(stream: Iterable[WeightedItem], k: int, seed: int = 1) -> List[int]:
    if k <= 0:
        raise WeightedSampleValidationError("k must be positive")
    rng = random.Random(seed)
    heap: List[Tuple[float, int]] = []
    for elem in stream:
        if elem.weight <= 0.0:
            raise WeightedSampleValidationError("weights must be strictly positive")
        u = rng.random() or 1e-12
        key = math.log(u) / elem.weight
        if len(heap) < k:
            heapq.heappush(heap, (key, elem.item_id))
        elif key > heap[0][0]:
            heapq.heapreplace(heap, (key, elem.item_id))
    return [item_id for _, item_id in sorted(heap, reverse=True)]
