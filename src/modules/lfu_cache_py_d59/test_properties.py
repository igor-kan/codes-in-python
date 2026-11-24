import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        c = LfuCachePy(3)
        for i in range(12): c.put(i % 5, i)
        self.assertLessEqual(len(c.vals), 3)

if __name__ == "__main__":
    unittest.main()
