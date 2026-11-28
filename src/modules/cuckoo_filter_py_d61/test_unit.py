import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        cf = CuckooFilter(capacity=256, bucket_size=4)
        items = list(range(80))
        for item in items:
            self.assertTrue(cf.insert(item))
        self.assertTrue(all(cf.contains(item) for item in items))
        self.assertEqual(cf.count, 80)
        self.assertEqual(cf.stats().capacity, 256)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
