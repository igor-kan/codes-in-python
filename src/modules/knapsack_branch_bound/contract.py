from typing import Protocol, Sequence
from models import KnapsackItem, KnapsackPlan


class KnapsackSolver(Protocol):
    def solve(self, items: Sequence[KnapsackItem], capacity: int) -> KnapsackPlan:
        ...
