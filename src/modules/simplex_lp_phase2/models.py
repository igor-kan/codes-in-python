from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class LinearProgram:
    c: Tuple[float, ...]
    a_rows: Tuple[Tuple[float, ...], ...]
    b: Tuple[float, ...]


@dataclass(frozen=True)
class SimplexSolution:
    status: str
    objective_value: float
    primal_x: Tuple[float, ...]
    pivots: int
