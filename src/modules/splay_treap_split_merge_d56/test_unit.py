import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        tr = DeterministicTreap()
        for v in [40, 10, 30, 20, 50]:
            tr.insert(v)
        self.assertEqual([tr.kth(i) for i in range(5)], [10, 20, 30, 40, 50])
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
