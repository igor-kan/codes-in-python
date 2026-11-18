import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        self.assertEqual(hopcroft_karp(3, 2, [(0,0),(1,0),(2,1)]).size, 2)

if __name__ == "__main__":
    unittest.main()
