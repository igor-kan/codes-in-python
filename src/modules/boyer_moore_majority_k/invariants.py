from collections import Counter
from typing import Dict, List
from exceptions import HeavyHitterInvariantError

def verify_matches_counter(stream: List[int], k: int, got: Dict[int, int]) -> None:
    thresh = len(stream) // k
    ref = {x: c for x, c in Counter(stream).items() if c > thresh}
    if ref != got:
        raise HeavyHitterInvariantError(f'heavy hitter mismatch: {got} vs {ref}')
