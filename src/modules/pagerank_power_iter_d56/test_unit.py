import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        scores = pagerank_scores(3, [(0, 1), (1, 2), (2, 0)])
        for s in scores:
            self.assertAlmostEqual(s, 1.0 / 3.0, places=6)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
