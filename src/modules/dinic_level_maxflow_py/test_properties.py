import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        self.assertEqual(dinic_max_flow(3, 0, 2, [(0,1,7),(1,2,5)]), 5)

if __name__ == "__main__":
    unittest.main()
