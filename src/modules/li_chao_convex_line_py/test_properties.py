import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        lc = LiChaoTree(32)
        lc.add_line(3, 1); lc.add_line(1, 10)
        self.assertEqual(lc.query(2), 7)

if __name__ == "__main__":
    unittest.main()
