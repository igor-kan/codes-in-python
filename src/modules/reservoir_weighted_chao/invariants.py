from typing import List
from exceptions import WeightedSampleInvariantError

def verify_distinct_k(sample_ids: List[int], k: int) -> None:
    if len(sample_ids) != k or len(set(sample_ids)) != k:
        raise WeightedSampleInvariantError('sample did not preserve K distinct elements')
