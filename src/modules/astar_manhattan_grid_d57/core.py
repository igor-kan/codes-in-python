from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def astar_grid_steps(grid: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]) -> int:
    rows, cols = len(grid), len(grid[0])
    sr, sc = start
    gr, gc = goal
    if grid[sr][sc] != 0 or grid[gr][gc] != 0:
        return -1

    def h(r: int, c: int) -> int:
        return abs(r - gr) + abs(c - gc)

    g_score: Dict[Tuple[int, int], int] = {(sr, sc): 0}
    pq: List[Tuple[int, int, Tuple[int, int]]] = [(h(sr, sc), 0, (sr, sc))]
    while pq:
        _, g, (r, c) = heapq.heappop(pq)
        if (r, c) == goal:
            return g
        if g > g_score.get((r, c), 10**9):
            continue
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                ng = g + 1
                if ng < g_score.get((nr, nc), 10**9):
                    g_score[(nr, nc)] = ng
                    heapq.heappush(pq, (ng + h(nr, nc), ng, (nr, nc)))
    return -1
