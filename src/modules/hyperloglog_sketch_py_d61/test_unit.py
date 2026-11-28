import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        hll = HyperLogLog(12)
        for i in range(2000):
            hll.add(i)
        est = hll.estimate()
        self.assertLess(abs(est - 2000) / 2000.0, 0.08)
        self.assertEqual(hll.report().registers, 4096)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
