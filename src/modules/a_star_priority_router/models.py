from dataclasses import dataclass
from typing import Tuple

Coord = Tuple[int, int]


@dataclass(frozen=True)
class GridMap:
    rows: int
    cols: int
    blocked: frozenset[Coord]


@dataclass(frozen=True)
class RouteResult:
    found: bool
    cost: int
    path: Tuple[Coord, ...]
    expanded_nodes: int
