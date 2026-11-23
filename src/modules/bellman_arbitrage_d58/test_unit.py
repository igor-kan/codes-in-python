import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        fair = [[1.0, 2.0, 4.0], [0.5, 1.0, 2.0], [0.25, 0.5, 1.0]]
        self.assertFalse(detect_fx_arbitrage(fair))
        arb = [[1.0, 2.0, 1.0], [0.5, 1.0, 2.0], [0.3, 0.5, 1.0]]
        self.assertTrue(detect_fx_arbitrage(arb))
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
