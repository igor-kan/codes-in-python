import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        res = viterbi_decode([0, 1, 2], [0.6, 0.4], [[0.7, 0.3], [0.4, 0.6]], [[0.5, 0.4, 0.1], [0.1, 0.3, 0.6]])
        self.assertEqual(res.states, (0, 0, 1))
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
