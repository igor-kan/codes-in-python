from typing import Protocol
from models import LinearProgram, SimplexSolution


class LinearProgramSolverProtocol(Protocol):
    def maximize(self, lp: LinearProgram, max_pivots: int) -> SimplexSolution:
        ...
