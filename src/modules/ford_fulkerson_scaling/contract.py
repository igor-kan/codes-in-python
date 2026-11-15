from typing import Protocol, Sequence
from models import DirectedCapEdge, MaxFlowReport


class MaxFlowSolverProtocol(Protocol):
    def solve(self, n: int, edges: Sequence[DirectedCapEdge], source: int, sink: int) -> MaxFlowReport:
        ...
