import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        mat = [[10, 19, 8], [10, 18, 7], [13, 16, 9]]
        tot, cols = hungarian_min_cost(mat)
        self.assertEqual(tot, 33)
        self.assertEqual(sorted(cols), [0, 1, 2])

if __name__ == "__main__":
    unittest.main()
