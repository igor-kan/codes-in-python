import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        res = exact_cover([[0, 1], [1, 2], [2, 3], [0, 3]], 4, limit=10)
        self.assertEqual(res.columns, 4)
        self.assertEqual(len(res.solutions), 2)
        self.assertEqual({tuple(sorted(sol)) for sol in res.solutions}, {(0, 2), (1, 3)})
        empty = exact_cover([[0, 1], [1, 2], [0, 2]], 3, limit=5)
        self.assertEqual(empty.solutions, ())
        with self.assertRaises(ValidationError):
            exact_cover([[0, 9]], 4)
        with self.assertRaises(ValidationError):
            exact_cover([[0, 0]], 4)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
