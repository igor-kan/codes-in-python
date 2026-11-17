from typing import List
from models import JobInterval
from exceptions import IntervalDpInvariantError

def verify_disjoint_weight(chosen: List[JobInterval], expected_total: int) -> None:
    for i in range(1, len(chosen)):
        if chosen[i - 1].end > chosen[i].start:
            raise IntervalDpInvariantError('overlapping intervals chosen')
    if sum(j.weight for j in chosen) != expected_total:
        raise IntervalDpInvariantError('weight sum mismatch')
