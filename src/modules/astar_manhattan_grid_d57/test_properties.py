import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        open_grid = [[0] * 4 for _ in range(4)]
        self.assertEqual(astar_grid_steps(open_grid, (0, 0), (3, 3)), 6)

if __name__ == "__main__":
    unittest.main()
