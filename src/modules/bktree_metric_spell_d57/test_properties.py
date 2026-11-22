import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        words = ["sort", "port", "fort", "mint", "tint"]
        bk = BkTree()
        for w in words: bk.add(w)
        self.assertEqual(bk.search("cort", 1), ["fort", "port", "sort"])

if __name__ == "__main__":
    unittest.main()
