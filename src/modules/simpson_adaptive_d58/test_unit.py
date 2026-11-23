import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        val = adaptive_simpson(math.sin, 0.0, math.pi, tol=1e-9)
        self.assertAlmostEqual(val, 2.0, places=8)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
