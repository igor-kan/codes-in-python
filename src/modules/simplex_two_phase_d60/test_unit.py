import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        sol = solve_lp_std([[1.0, 1.0], [2.0, 1.0]], [4.0, 6.0], [3.0, 2.0])
        self.assertAlmostEqual(sol.objective, 10.0, places=6)
        self.assertAlmostEqual(sol.primal[0], 2.0, places=6)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
