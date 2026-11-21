import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        tr = DeterministicTreap()
        for v in [9, 2, 7, 1, 5]:
            tr.insert(v)
        self.assertEqual([tr.kth(i) for i in range(5)], sorted([9, 2, 7, 1, 5]))

if __name__ == "__main__":
    unittest.main()
