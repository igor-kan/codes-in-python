import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        pts = [(2.0, 3.0), (5.0, 4.0), (9.0, 6.0), (4.0, 7.0), (8.0, 1.0)]
        tree = build_kdtree(pts)
        self.assertAlmostEqual(kdtree_nearest_sq(tree, (5.5, 4.2)), 0.29, places=9)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
