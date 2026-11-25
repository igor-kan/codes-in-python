import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        a, b = "intention", "execution"
        steps = hirschberg_align(a, b)
        self.assertEqual(edit_cost(steps), 5)
        self.assertEqual("".join(s.a_ch for s in steps if s.a_ch != "-"), a)
        self.assertEqual("".join(s.b_ch for s in steps if s.b_ch != "-"), b)

if __name__ == "__main__":
    unittest.main()
