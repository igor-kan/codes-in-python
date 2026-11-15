import heapq
from typing import Dict, List, Tuple
from models import Coord, GridMap, RouteResult


def manhattan(a: Coord, b: Coord) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


class AStarGridRouter:
    def find_path(self, grid: GridMap, start: Coord, goal: Coord) -> RouteResult:
        if start in grid.blocked or goal in grid.blocked:
            return RouteResult(found=False, cost=-1, path=(), expanded_nodes=0)
        pq: List[Tuple[int, int, Coord]] = [(manhattan(start, goal), 0, start)]
        g_score: Dict[Coord, int] = {start: 0}
        parent: Dict[Coord, Coord] = {}
        closed: set[Coord] = set()
        expanded = 0

        while pq:
            _, g, cur = heapq.heappop(pq)
            if cur in closed:
                continue
            closed.add(cur)
            expanded += 1
            if cur == goal:
                rev = [goal]
                while rev[-1] in parent:
                    rev.append(parent[rev[-1]])
                rev.reverse()
                return RouteResult(found=True, cost=g, path=tuple(rev), expanded_nodes=expanded)

            r, c = cur
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < grid.rows and 0 <= nc < grid.cols:
                    nxt = (nr, nc)
                    if nxt in grid.blocked or nxt in closed:
                        continue
                    tentative = g + 1
                    if tentative < g_score.get(nxt, 1 << 30):
                        g_score[nxt] = tentative
                        parent[nxt] = cur
                        heapq.heappush(pq, (tentative + manhattan(nxt, goal), tentative, nxt))
        return RouteResult(found=False, cost=-1, path=(), expanded_nodes=expanded)
