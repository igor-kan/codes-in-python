import random
import unittest
from core import FloydCycleDetector
from fast_path import brent_detect
from invariants import verify_cycle_signature


class TestRandomFunctionalGraphs(unittest.TestCase):
    def test_floyd_vs_brent(self) -> None:
        rng = random.Random(303)
        det = FloydCycleDetector()
        for _ in range(30):
            n = 64
            nxt = [rng.randrange(n) for _ in range(n)]
            fn = lambda u, arr=nxt: arr[u]
            start = rng.randrange(n)
            f_sig = det.detect(fn, start)
            b_sig = brent_detect(fn, start)
            self.assertEqual(f_sig, b_sig)
            verify_cycle_signature(fn, start, f_sig)


if __name__ == "__main__":
    unittest.main()
