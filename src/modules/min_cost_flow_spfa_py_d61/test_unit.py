import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        edges = [(0, 1, 2, 1), (0, 2, 2, 5), (1, 3, 2, 1), (2, 3, 2, 5)]
        res = min_cost_flow(4, 0, 3, edges)
        self.assertEqual(res.flow, 4)
        self.assertEqual(res.cost, 24)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
