import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        tot, cols = hungarian_min_cost([[4, 1, 3], [2, 0, 5], [3, 2, 2]])
        self.assertEqual(tot, 5)
        self.assertEqual(len(set(cols)), 3)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
