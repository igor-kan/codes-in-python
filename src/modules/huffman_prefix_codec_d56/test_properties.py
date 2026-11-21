import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        codes = build_huffman_codes({"a": 50, "b": 10, "c": 5, "d": 1})
        self.assertLessEqual(len(codes["a"]), len(codes["d"]))

if __name__ == "__main__":
    unittest.main()
