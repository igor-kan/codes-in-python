import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        bk = BkTree()
        for w in ["book", "books", "cake", "boo", "cape", "cart"]:
            bk.add(w)
        self.assertEqual(bk.search("caek", 2), ["cake", "cape", "cart"])
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
