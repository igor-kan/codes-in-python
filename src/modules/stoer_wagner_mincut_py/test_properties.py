import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        self.assertEqual(stoer_wagner_mincut(3, [[0,10,0],[10,0,2],[0,2,0]]).weight, 2)

if __name__ == "__main__":
    unittest.main()
