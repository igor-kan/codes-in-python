import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        self.assertEqual(aho_corasick_count(['ab', 'aba', 'ba'], 'ababa').hits, 6)

if __name__ == "__main__":
    unittest.main()
