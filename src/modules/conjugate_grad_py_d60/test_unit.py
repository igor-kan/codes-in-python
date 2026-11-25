import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        a = [[4.0, 1.0], [1.0, 3.0]]
        b = [1.0, 2.0]
        rep = conjugate_gradient(a, b)
        self.assertAlmostEqual(rep.x[0], 1.0 / 11.0, places=8)
        self.assertAlmostEqual(rep.x[1], 7.0 / 11.0, places=8)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
