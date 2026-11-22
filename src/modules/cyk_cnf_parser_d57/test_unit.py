import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        terms = {"a": ["A"], "b": ["B"]}
        bins = [("S", "A", "B"), ("S", "A", "X"), ("X", "S", "B")]
        self.assertTrue(cyk_accepts(terms, bins, "S", ["a", "a", "b", "b"]))
        self.assertFalse(cyk_accepts(terms, bins, "S", ["a", "b", "b"]))
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
