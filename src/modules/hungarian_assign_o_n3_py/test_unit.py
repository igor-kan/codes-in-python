import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        self.assertEqual(hungarian_min_cost([[1,2,3],[2,4,6],[3,6,9]]).cost, 10)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
