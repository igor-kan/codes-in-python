import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        known = {1: 1, 2: 0, 3: 0, 4: 2, 5: 10, 6: 4, 7: 40, 8: 92}
        for n in range(1, 9):
            self.assertEqual(count_n_queens(n), known[n])
        for n in range(1, 9):
            board = first_n_queens(n)
            if n in (2, 3):
                self.assertEqual(board, ())
                continue
            self.assertEqual(len(board), n)
            self.assertEqual(len(set(board)), n)
            for r1 in range(n):
                for r2 in range(r1 + 1, n):
                    self.assertNotEqual(abs(board[r1] - board[r2]), r2 - r1)
        res = queens_result(7)
        self.assertEqual(res.count, 40)
        self.assertEqual(len(res.first), 7)

if __name__ == "__main__":
    unittest.main()
