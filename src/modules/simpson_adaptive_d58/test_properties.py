import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        poly = lambda x: x * x * x + x
        self.assertAlmostEqual(adaptive_simpson(poly, 0.0, 2.0), 6.0, places=9)

if __name__ == "__main__":
    unittest.main()
