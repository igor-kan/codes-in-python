import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        self.assertEqual(solve_blossom_matching(5, [(0,1),(1,2),(2,3),(3,4),(4,0)]).pairs, 2)

if __name__ == "__main__":
    unittest.main()
