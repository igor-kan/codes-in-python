import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        bf = IntBitBloom(256, 4)
        for k in [10, 25, 99, 1024]: bf.add(k)
        for k in [10, 25, 99, 1024]: self.assertTrue(bf.might_contain(k))
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
