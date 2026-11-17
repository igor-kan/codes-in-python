import unittest
from models import WeightedItem
from core import ares_sample
from invariants import verify_distinct_k

class TestAres(unittest.TestCase):
    def test_heavy_item_bias(self):
        items = [WeightedItem(0, 1000.0)] + [WeightedItem(i, 0.01) for i in range(1, 20)]
        hits = sum(1 for s in range(30) if 0 in ares_sample(items, 3, seed=s + 1))
        self.assertGreaterEqual(hits, 28)
        verify_distinct_k(ares_sample(items, 5, seed=7), 5)

if __name__ == '__main__':
    unittest.main()
