from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class CgSolution:
    x: List[float]
    iters: int
    residual: float
