import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        g = [[0,2,0,0,3],[2,0,3,0,2],[0,3,0,4,0],[0,0,4,0,1],[3,2,0,1,0]]; self.assertEqual(stoer_wagner_mincut(5, g).weight, 4)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
