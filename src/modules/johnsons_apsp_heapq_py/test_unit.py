import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        dm = johnson_apsp(4, [(0,1,4),(0,2,5),(1,2,-3),(2,3,2)]).dist; self.assertEqual(dm[0][3], 3); self.assertEqual(dm[1][3], -1)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
