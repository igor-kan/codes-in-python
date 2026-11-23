import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        p, _ = viterbi_log_path([0.8, 0.2], [[0.9, 0.1], [0.2, 0.8]], [[0.9, 0.1], [0.1, 0.9]], [0, 0, 1, 1])
        self.assertEqual(p, [0, 0, 1, 1])
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
