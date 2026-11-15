import unittest
from core import AStarGridRouter
from fast_path import flat_astar_distance
from invariants import verify_route
from models import GridMap
from validation import validate_route_request


class TestAStarRouter(unittest.TestCase):
    def test_detour_around_wall(self) -> None:
        walls = frozenset({(1, 1), (2, 1), (3, 1), (0, 3), (1, 3), (2, 3)})
        grid = GridMap(rows=5, cols=5, blocked=walls)
        validate_route_request(grid, (0, 0), (4, 4))
        res = AStarGridRouter().find_path(grid, (0, 0), (4, 4))
        verify_route(grid, (0, 0), (4, 4), res)
        self.assertTrue(res.found)
        self.assertEqual(res.cost, flat_astar_distance(grid, (0, 0), (4, 4)))


if __name__ == "__main__":
    unittest.main()
