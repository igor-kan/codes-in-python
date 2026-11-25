import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        a = [[5.0, 1.0, 0.0], [1.0, 4.0, 1.0], [0.0, 1.0, 3.0]]
        b = [6.0, 6.0, 4.0]
        rep = conjugate_gradient(a, b)
        self.assertLess(rep.residual, 1e-9)
        for xi in rep.x:
            self.assertAlmostEqual(xi, 1.0, places=7)

if __name__ == "__main__":
    unittest.main()
