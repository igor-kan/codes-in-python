from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class PageRankResult:
    ranks: Tuple[float, ...]
    iterations: int
    l1_residual: float
