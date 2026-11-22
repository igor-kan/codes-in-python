import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        d, ops = levenshtein_with_trace("abc", "yabd")
        self.assertEqual(d, sum(1 for op in ops if op != "M"))

if __name__ == "__main__":
    unittest.main()
