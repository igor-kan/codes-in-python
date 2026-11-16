from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class AssignmentResult:
    row_to_col: Tuple[int, ...]
    total_cost: float
    row_duals: Tuple[float, ...]
    col_duals: Tuple[float, ...]
