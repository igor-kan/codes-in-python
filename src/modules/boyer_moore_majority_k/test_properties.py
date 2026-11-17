import random, unittest
from concurrency import parallel_heavy_hitters
from invariants import verify_matches_counter

class TestHeavyProps(unittest.TestCase):
    def test_random_streams(self):
        rng = random.Random(42)
        s1 = [rng.randint(0, 6) for _ in range(120)] + [99]*45
        s2 = [rng.randint(0, 8) for _ in range(100)] + [77]*35
        outs = parallel_heavy_hitters([s1, s2], 4)
        verify_matches_counter(s1, 4, outs[0])
        verify_matches_counter(s2, 4, outs[1])

if __name__ == '__main__':
    unittest.main()
