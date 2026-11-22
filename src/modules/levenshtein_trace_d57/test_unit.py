import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        d, ops = levenshtein_with_trace("kitten", "sitting")
        self.assertEqual(d, 3)
        self.assertEqual(sum(1 for op in ops if op != "M"), 3)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
