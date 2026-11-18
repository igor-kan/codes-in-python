import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        self.assertEqual(query_rmq_idx(build_cartesian([5, 2, 8]), 0, 2), 1)

if __name__ == "__main__":
    unittest.main()
