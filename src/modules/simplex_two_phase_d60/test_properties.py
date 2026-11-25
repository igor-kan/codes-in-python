import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        sol = solve_lp_std([[2.0, 1.0], [1.0, 2.0]], [8.0, 8.0], [1.0, 1.0])
        self.assertLessEqual(2.0 * sol.primal[0] + sol.primal[1], 8.0 + 1e-7)

if __name__ == "__main__":
    unittest.main()
