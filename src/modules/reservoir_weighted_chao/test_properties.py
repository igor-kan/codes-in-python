import unittest
from models import WeightedItem
from concurrency import parallel_trials
from invariants import verify_distinct_k

class TestAresProps(unittest.TestCase):
    def test_parallel_trials(self):
        items = [WeightedItem(i, float(i + 1)) for i in range(25)]
        trials = parallel_trials(items, 6, [11, 22, 33])
        for tr in trials:
            verify_distinct_k(tr, 6)

if __name__ == '__main__':
    unittest.main()
