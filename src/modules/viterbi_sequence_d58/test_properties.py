import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        p, sc = viterbi_log_path([0.5, 0.5], [[0.7, 0.3], [0.3, 0.7]], [[0.8, 0.2], [0.2, 0.8]], [0, 1])
        self.assertEqual(len(p), 2)
        self.assertLess(sc, 0.0)

if __name__ == "__main__":
    unittest.main()
