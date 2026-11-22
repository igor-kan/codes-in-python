import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        terms = {"x": ["V"]}
        bins = [("E", "V", "E")]
        self.assertFalse(cyk_accepts(terms, bins, "E", ["x", "x"]))

if __name__ == "__main__":
    unittest.main()
