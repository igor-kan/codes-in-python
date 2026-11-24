import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        A = [[5.0, 0.0], [0.0, 2.0]]
        x = cg_solve(A, [15.0, 8.0])
        self.assertAlmostEqual(x[0], 3.0, places=9)

if __name__ == "__main__":
    unittest.main()
