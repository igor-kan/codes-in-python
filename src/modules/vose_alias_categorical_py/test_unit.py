import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        tbl = build_alias_table([1.0, 3.0])
        hits = [sample_alias(tbl, b, (k + 0.5) / 4.0) for b in range(2) for k in range(4)]
        self.assertEqual(hits.count(0), 2)
        self.assertEqual(hits.count(1), 6)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
