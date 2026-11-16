from typing import Protocol, Sequence
from models import AssignmentResult


class BipartiteSolver(Protocol):
    def solve_min_cost(self, cost_matrix: Sequence[Sequence[float]]) -> AssignmentResult:
        ...
