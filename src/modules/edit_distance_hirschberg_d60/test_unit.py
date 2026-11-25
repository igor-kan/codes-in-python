import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        steps = hirschberg_align("kitten", "sitting")
        self.assertEqual(edit_cost(steps), 3)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
