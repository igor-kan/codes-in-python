import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        pts = [(float(i * 3 % 11), float(i * 5 % 13)) for i in range(15)]
        tree = build_kd_tree(pts)
        q = (4.2, 6.1)
        got, gd = kd_nearest(tree, q)
        exact = min(math.hypot(p[0] - q[0], p[1] - q[1]) for p in pts)
        self.assertAlmostEqual(gd, exact, places=9)
        self.assertIsNotNone(got)

if __name__ == "__main__":
    unittest.main()
