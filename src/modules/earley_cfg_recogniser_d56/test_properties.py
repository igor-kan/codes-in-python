import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        expr = {"E": [("E", "+", "n"), ("n",)]}
        self.assertTrue(earley_accepts(expr, "E", ["n", "+", "n", "+", "n"]))
        self.assertFalse(earley_accepts(expr, "E", ["+", "n"]))

if __name__ == "__main__":
    unittest.main()
