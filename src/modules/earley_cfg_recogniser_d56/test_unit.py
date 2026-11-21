import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        g = {"S": [("(", "S", ")"), ()]}
        self.assertTrue(earley_accepts(g, "S", ["(", "(", ")", ")"]))
        self.assertFalse(earley_accepts(g, "S", ["(", ")", ")"]))
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
