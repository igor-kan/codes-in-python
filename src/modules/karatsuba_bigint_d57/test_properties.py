import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        for x, y in [(99999, 88888), (10**18 + 7, 10**15 + 9)]:
            self.assertEqual(karatsuba_mul(x, y), x * y)

if __name__ == "__main__":
    unittest.main()
