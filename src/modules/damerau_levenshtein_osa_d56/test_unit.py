import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        self.assertEqual(osa_edit_distance("ca", "ac"), 1)
        self.assertEqual(osa_edit_distance("kitten", "sitting"), 3)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
