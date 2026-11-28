import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        data = [5, 3, 8, 1, 3, 9, 3, 0]
        wm = WaveletMatrix(data)
        self.assertEqual(wm.rank(3, 0, 8), 3)
        self.assertEqual(wm.kth_smallest(0, 0, 8), 0)
        self.assertEqual(wm.kth_smallest(7, 0, 8), 9)
        self.assertEqual(wm.kth_smallest(1, 2, 6), 3)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
