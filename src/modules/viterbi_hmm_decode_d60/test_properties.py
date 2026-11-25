import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        res = viterbi_decode([0, 0, 1, 1], [0.5, 0.5], [[0.9, 0.1], [0.1, 0.9]], [[0.9, 0.1], [0.1, 0.9]])
        self.assertEqual(res.states, (0, 0, 1, 1))

if __name__ == "__main__":
    unittest.main()
