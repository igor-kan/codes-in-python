import unittest
from models import JobInterval
from core import solve_weighted_intervals
from invariants import verify_disjoint_weight

class TestWis(unittest.TestCase):
    def test_dp(self):
        jobs = [JobInterval(1,3,5), JobInterval(2,5,6), JobInterval(4,6,5), JobInterval(6,7,4)]
        tot, chosen = solve_weighted_intervals(jobs)
        verify_disjoint_weight(chosen, tot)
        self.assertEqual(tot, 14)

if __name__ == '__main__':
    unittest.main()
