import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        span, d = dag_longest_path(4, [(0, 1, 5), (1, 2, 7), (2, 3, 1)])
        self.assertEqual(d[3], 13)

if __name__ == "__main__":
    unittest.main()
