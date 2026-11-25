import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        pts = [(2.0, 3.0), (5.0, 4.0), (9.0, 6.0), (4.0, 7.0), (8.0, 1.0), (7.0, 2.0)]
        tree = build_kd_tree(pts)
        pt, _ = kd_nearest(tree, (9.0, 2.0))
        self.assertEqual(pt, (8.0, 1.0))
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
