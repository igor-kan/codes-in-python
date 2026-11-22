import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        pts = [(0.0, 0.0), (10.0, 10.0), (3.0, 4.0), (1.0, 9.0)]
        tree = build_kdtree(pts)
        q = (2.8, 3.5)
        brute = min((p[0] - q[0])**2 + (p[1] - q[1])**2 for p in pts)
        self.assertAlmostEqual(kdtree_nearest_sq(tree, q), brute, places=10)

if __name__ == "__main__":
    unittest.main()
