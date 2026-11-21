import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        scores = pagerank_scores(4, [(0, 2), (1, 2), (3, 2)])
        self.assertAlmostEqual(sum(scores), 1.0, places=7)
        self.assertGreater(scores[2], scores[0])

if __name__ == "__main__":
    unittest.main()
