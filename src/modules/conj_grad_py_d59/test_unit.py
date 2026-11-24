import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        A = [[4.0, 1.0], [1.0, 3.0]]
        x = cg_solve(A, [1.0, 2.0])
        self.assertAlmostEqual(4.0 * x[0] + x[1], 1.0, places=8)
        self.assertAlmostEqual(x[0] + 3.0 * x[1], 2.0, places=8)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
