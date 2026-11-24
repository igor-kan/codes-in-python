import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        inf = 1e15
        m = [[0.0, 3.0, inf], [inf, 0.0, 4.0], [1.0, inf, 0.0]]
        neg, d = floyd_apsp(m)
        self.assertFalse(neg)
        self.assertEqual(d[0][2], 7.0)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
