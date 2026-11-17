from typing import Dict, List
from models import HeavyHitterResult
from exceptions import HeavyHitterValidationError


def misra_gries_heavy(stream: List[int], k: int) -> HeavyHitterResult:
    if k < 2:
        raise HeavyHitterValidationError("k must be >= 2")
    counters: Dict[int, int] = {}
    for x in stream:
        if x in counters:
            counters[x] += 1
        elif len(counters) < k - 1:
            counters[x] = 1
        else:
            drop = []
            for key in counters:
                counters[key] -= 1
                if counters[key] == 0:
                    drop.append(key)
            for key in drop:
                del counters[key]
    exact: Dict[int, int] = {key: 0 for key in counters}
    for x in stream:
        if x in exact:
            exact[x] += 1
    thresh = len(stream) // k
    verified = {key: cnt for key, cnt in exact.items() if cnt > thresh}
    return HeavyHitterResult(candidates=counters, verified_counts=verified)
