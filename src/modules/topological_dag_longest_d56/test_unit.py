import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        span, d = dag_longest_path(5, [(0, 1, 3), (0, 2, 2), (1, 3, 4), (2, 3, 6), (3, 4, 2)])
        self.assertEqual(span, 10)
        self.assertEqual(d[4], 10)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
