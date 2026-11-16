from typing import Optional, Sequence, Tuple
from exceptions import PageRankDimensionError, PageRankDomainError


def validate_pagerank_inputs(
    n: int,
    edges: Sequence[Tuple[int, int]],
    damping: float,
    tol: float,
    personalization: Optional[Sequence[float]],
) -> Tuple[float, ...]:
    if n <= 0:
        raise PageRankDimensionError("n must be > 0")
    if not (0.0 < damping < 1.0) or tol <= 0.0:
        raise PageRankDomainError("invalid damping or tolerance")
    for u, v in edges:
        if u < 0 or u >= n or v < 0 or v >= n:
            raise PageRankDomainError("edge vertex out of bounds")
    if personalization is None:
        return tuple([1.0 / n] * n)
    if len(personalization) != n:
        raise PageRankDimensionError("personalization length mismatch")
    if any(x < 0.0 for x in personalization) or sum(personalization) <= 0.0:
        raise PageRankDomainError("invalid personalization distribution")
    tot = sum(personalization)
    return tuple(x / tot for x in personalization)
