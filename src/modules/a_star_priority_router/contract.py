from typing import Protocol
from models import Coord, GridMap, RouteResult


class GridRouterProtocol(Protocol):
    def find_path(self, grid: GridMap, start: Coord, goal: Coord) -> RouteResult:
        ...
