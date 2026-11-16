from typing import Sequence, Tuple
from exceptions import TarjanSccDimensionError, TarjanSccDomainError


def validate_digraph(n: int, edges: Sequence[Tuple[int, int]]) -> None:
    if n <= 0:
        raise TarjanSccDimensionError("vertex count n must be positive")
    for u, v in edges:
        if u < 0 or u >= n or v < 0 or v >= n:
            raise TarjanSccDomainError(f"edge ({u}, {v}) out of bounds [0, {n})")
