from typing import Protocol, Sequence, Tuple
from models import SccResult


class SccAnalyzer(Protocol):
    def decompose(self, n: int, edges: Sequence[Tuple[int, int]]) -> SccResult:
        ...
