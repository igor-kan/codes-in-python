import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        rows = [[0, 1], [0, 2], [1, 2], [0, 1, 2], [2]]
        res = exact_cover(rows, 3, limit=10 ** 9)
        def brute() -> int:
            count = 0
            for mask in range(1 << len(rows)):
                cover: List[int] = []
                for idx, row in enumerate(rows):
                    if (mask >> idx) & 1:
                        cover.extend(row)
                if len(cover) == 3 and len(set(cover)) == 3:
                    count += 1
            return count
        self.assertEqual(len(res.solutions), brute())
        for solution in res.solutions:
            self.assertEqual(len(solution), len(set(solution)))
            covered: List[int] = []
            for idx in solution:
                covered.extend(rows[idx])
            self.assertEqual(sorted(covered), [0, 1, 2])
        limited = exact_cover(rows, 3, limit=1)
        self.assertEqual(len(limited.solutions), 1)

if __name__ == "__main__":
    unittest.main()
