import heapq
from typing import List, Tuple
from models import Coord, GridMap


def flat_astar_distance(grid: GridMap, start: Coord, goal: Coord) -> int:
    rows, cols = grid.rows, grid.cols
    n = rows * cols
    blocked = bytearray(n)
    for r, c in grid.blocked:
        blocked[r * cols + c] = 1
    s_idx = start[0] * cols + start[1]
    g_idx = goal[0] * cols + goal[1]
    if blocked[s_idx] or blocked[g_idx]:
        return -1
    dist = [1 << 29] * n
    dist[s_idx] = 0
    gx, gy = goal
    pq: List[Tuple[int, int]] = [(abs(start[0] - gx) + abs(start[1] - gy), s_idx)]
    while pq:
        f, u = heapq.heappop(pq)
        g = dist[u]
        if u == g_idx:
            return g
        ur, uc = divmod(u, cols)
        if f > g + abs(ur - gx) + abs(uc - gy):
            continue
        for nr, nc in ((ur - 1, uc), (ur + 1, uc), (ur, uc - 1), (ur, uc + 1)):
            if 0 <= nr < rows and 0 <= nc < cols:
                v = nr * cols + nc
                if not blocked[v] and g + 1 < dist[v]:
                    dist[v] = g + 1
                    heapq.heappush(pq, (g + 1 + abs(nr - gx) + abs(nc - gy), v))
    return -1
