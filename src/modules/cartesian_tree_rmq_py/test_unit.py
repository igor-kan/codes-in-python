import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        ct = build_cartesian([9, 3, 7, 1, 8, 12, 10, 20, 15, 18, 5])
        self.assertEqual(query_rmq_idx(ct, 0, 2), 1)
        self.assertEqual(query_rmq_idx(ct, 4, 10), 10)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
