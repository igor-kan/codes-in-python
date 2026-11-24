import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        c = LfuCachePy(2)
        c.put(1, 10); c.put(2, 20)
        self.assertEqual(c.get(1), 10)
        c.put(3, 30)
        self.assertEqual(c.get(2), -1)
        self.assertEqual(c.get(3), 30)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
