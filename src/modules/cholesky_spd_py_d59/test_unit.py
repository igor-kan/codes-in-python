import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        A = [[4.0, 12.0, -16.0], [12.0, 37.0, -43.0], [-16.0, -43.0, 98.0]]
        L = cholesky_lower(A)
        self.assertAlmostEqual(L[0][0], 2.0, places=9)
        self.assertAlmostEqual(L[2][2], 3.0, places=9)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
