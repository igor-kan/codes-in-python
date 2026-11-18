import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        self.assertEqual(hopcroft_karp(4, 4, [(0,0),(0,1),(1,0),(2,2),(2,3),(3,2)]).size, 4)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
