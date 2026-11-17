from typing import List, Protocol
from models import CgSolution

class SpdSolver(Protocol):
    def solve(self, a: List[List[float]], b: List[float]) -> CgSolution: ...
