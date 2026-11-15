from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class DirectedCapEdge:
    u: int
    v: int
    cap: int


@dataclass(frozen=True)
class MaxFlowReport:
    max_flow: int
    min_cut_source_side: Tuple[int, ...]
