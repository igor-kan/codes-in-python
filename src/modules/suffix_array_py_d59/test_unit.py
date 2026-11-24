import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        sa, lcp, d = suffix_array_and_lcp("banana")
        self.assertEqual(sa, [5, 3, 1, 0, 4, 2])
        self.assertEqual(max(lcp), 3)
        self.assertEqual(d, 15)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
