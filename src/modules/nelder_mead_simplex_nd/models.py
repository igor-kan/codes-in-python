from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class SimplexResult:
    x: List[float]
    fval: float
    iters: int
