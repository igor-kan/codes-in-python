import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        self.assertEqual(dinic_max_flow(4, 0, 3, [(0,1,10),(0,2,10),(1,2,2),(1,3,8),(2,3,10)]), 18)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
