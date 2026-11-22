import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        g = [[0, 1, 0], [0, 0, 0], [1, 1, 0]]
        self.assertEqual(astar_grid_steps(g, (0, 0), (2, 2)), 4)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
