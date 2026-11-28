import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        data = [7, 1, 4, 4, 2, 9, 0, 6, 4]
        wm = WaveletMatrix(data)
        for value in range(10):
            self.assertEqual(wm.rank(value, 0, len(data)), data.count(value))
        for lo in range(len(data)):
            for hi in range(lo + 1, len(data) + 1):
                segment = sorted(data[lo:hi])
                for k in range(len(segment)):
                    self.assertEqual(wm.kth_smallest(k, lo, hi), segment[k])
        self.assertEqual(wm.rank(4, 1, 4), 2)
        self.assertEqual(wm.rank(5, 1, 4), 0)

if __name__ == "__main__":
    unittest.main()
