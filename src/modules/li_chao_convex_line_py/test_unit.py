import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        lc = LiChaoTree(64)
        lc.add_line(2, 10); lc.add_line(-1, 50); lc.add_line(0, 25)
        self.assertEqual(lc.query(5), 20)
        self.assertEqual(lc.query(40), 10)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
