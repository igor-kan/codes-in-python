import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        qt = QuadNode(0.0, 0.0, 100.0, 100.0, cap=2)
        pts = [(10.0, 10.0), (20.0, 20.0), (80.0, 80.0), (25.0, 25.0)]
        for p in pts: qt.insert(p)
        self.assertEqual(sorted(qt.query_box(5.0, 5.0, 30.0, 30.0)), [(10.0, 10.0), (20.0, 20.0), (25.0, 25.0)])
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
