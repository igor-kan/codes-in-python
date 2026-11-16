from typing import Optional, Protocol, Sequence, Tuple
from models import PageRankResult


class CentralityEngine(Protocol):
    def compute(
        self,
        n: int,
        edges: Sequence[Tuple[int, int]],
        damping: float = 0.85,
        tol: float = 1e-10,
        max_iter: int = 200,
        personalization: Optional[Sequence[float]] = None,
    ) -> PageRankResult:
        ...
