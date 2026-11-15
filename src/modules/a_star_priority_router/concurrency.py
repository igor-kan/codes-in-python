from concurrent.futures import ThreadPoolExecutor
from typing import List, Sequence, Tuple
from core import AStarGridRouter
from models import Coord, GridMap, RouteResult


def solve_batch_routes(
    grid: GridMap, pairs: Sequence[Tuple[Coord, Coord]], workers: int = 2
) -> List[RouteResult]:
    router = AStarGridRouter()
    with ThreadPoolExecutor(max_workers=workers) as pool:
        return list(pool.map(lambda ab: router.find_path(grid, ab[0], ab[1]), pairs))
