import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        self.assertEqual(johnson_apsp(3, [(0,1,10),(0,2,2),(2,1,-1)]).dist[0][1], 1)

if __name__ == "__main__":
    unittest.main()
