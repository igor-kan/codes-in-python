import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        self.assertEqual(solve_blossom_matching(6, [(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(5,3)]).pairs, 3)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
