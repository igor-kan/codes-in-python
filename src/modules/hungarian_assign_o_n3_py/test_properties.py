import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        self.assertEqual(hungarian_min_cost([[10,1],[2,10]]).cost, 3)

if __name__ == "__main__":
    unittest.main()
