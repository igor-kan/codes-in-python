from typing import List
from exceptions import HeavyHitterValidationError

def validate_stream(stream: List[int], k: int) -> None:
    if k < 2:
        raise HeavyHitterValidationError('require k >= 2')
