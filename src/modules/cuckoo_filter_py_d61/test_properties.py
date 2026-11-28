import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        cf = CuckooFilter(capacity=128, bucket_size=4)
        payload = [("k", i) for i in range(40)]
        for item in payload:
            self.assertTrue(cf.insert(item))
        for item in payload:
            self.assertTrue(cf.contains(item))
        for item in payload:
            self.assertTrue(cf.remove(item))
        self.assertEqual(cf.count, 0)
        for item in payload:
            self.assertFalse(cf.contains(item))

if __name__ == "__main__":
    unittest.main()
