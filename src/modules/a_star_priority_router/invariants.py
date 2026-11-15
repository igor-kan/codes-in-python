from collections import deque
from models import Coord, GridMap, RouteResult


def bfs_shortest_distance(grid: GridMap, start: Coord, goal: Coord) -> int:
    if start in grid.blocked or goal in grid.blocked:
        return -1
    q = deque([(start, 0)])
    seen = {start}
    while q:
        (r, c), d = q.popleft()
        if (r, c) == goal:
            return d
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if 0 <= nr < grid.rows and 0 <= nc < grid.cols and (nr, nc) not in seen and (nr, nc) not in grid.blocked:
                seen.add((nr, nc))
                q.append(((nr, nc), d + 1))
    return -1


def verify_route(grid: GridMap, start: Coord, goal: Coord, res: RouteResult) -> None:
    oracle = bfs_shortest_distance(grid, start, goal)
    assert res.cost == oracle
    if res.found:
        assert res.path[0] == start and res.path[-1] == goal
        assert len(res.path) == res.cost + 1
        for a, b in zip(res.path, res.path[1:]):
            assert a not in grid.blocked and b not in grid.blocked
            assert abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1
