import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        self.assertEqual(count_n_queens(1), 1)
        self.assertEqual(count_n_queens(4), 2)
        self.assertEqual(count_n_queens(5), 10)
        self.assertEqual(count_n_queens(8), 92)
        first = first_n_queens(4)
        self.assertEqual(len(first), 4)
        self.assertEqual(len(set(first)), 4)
        self.assertEqual(queens_result(6).count, 4)
        self.assertEqual(first_n_queens(2), ())
        with self.assertRaises(ValidationError):
            count_n_queens(0)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
