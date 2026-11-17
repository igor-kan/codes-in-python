import unittest
from core import misra_gries_heavy
from invariants import verify_matches_counter

class TestHeavy(unittest.TestCase):
    def test_heavy_k4(self):
        s = [1]*10 + [2]*10 + [3]*4 + [4, 5, 6, 7, 8]
        res = misra_gries_heavy(s, 4)
        verify_matches_counter(s, 4, res.verified_counts)

if __name__ == '__main__':
    unittest.main()
