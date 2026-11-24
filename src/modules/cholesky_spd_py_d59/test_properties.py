import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        A = [[9.0, 3.0], [3.0, 10.0]]
        L = cholesky_lower(A)
        rec11 = sum(L[1][k] * L[1][k] for k in range(2))
        self.assertAlmostEqual(rec11, 10.0, places=9)

if __name__ == "__main__":
    unittest.main()
