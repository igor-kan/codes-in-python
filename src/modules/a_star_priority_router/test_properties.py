import random
import unittest
from core import AStarGridRouter
from invariants import verify_route
from models import GridMap


class TestAStarProperties(unittest.TestCase):
    def test_random_mazes(self) -> None:
        rng = random.Random(77)
        router = AStarGridRouter()
        for _ in range(25):
            walls = frozenset((rng.randrange(8), rng.randrange(8)) for _ in range(18)) - {(0, 0), (7, 7)}
            grid = GridMap(rows=8, cols=8, blocked=walls)
            res = router.find_path(grid, (0, 0), (7, 7))
            verify_route(grid, (0, 0), (7, 7), res)


if __name__ == "__main__":
    unittest.main()
