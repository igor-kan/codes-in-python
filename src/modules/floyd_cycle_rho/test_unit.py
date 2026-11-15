import unittest
from core import FloydCycleDetector
from fast_path import brent_detect
from invariants import verify_cycle_signature
from validation import validate_budget


class TestCycleDetectors(unittest.TestCase):
    def test_lcg_cycle(self) -> None:
        validate_budget(10000)
        fn = lambda x: (5 * x + 3) % 16
        f_sig = FloydCycleDetector().detect(fn, 1)
        b_sig = brent_detect(fn, 1)
        self.assertEqual(f_sig, b_sig)
        verify_cycle_signature(fn, 1, f_sig)


if __name__ == "__main__":
    unittest.main()
