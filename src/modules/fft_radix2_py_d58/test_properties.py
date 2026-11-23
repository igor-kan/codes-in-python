import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        imp = [1.0 + 0j, 0j, 0j, 0j]
        sp = dft_rad2(imp)
        for v in sp:
            self.assertAlmostEqual(abs(v), 1.0, places=9)

if __name__ == "__main__":
    unittest.main()
