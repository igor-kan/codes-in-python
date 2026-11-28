import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        self.assertEqual(segmented_primes(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        self.assertEqual(prime_pi(1000), 168)
        self.assertEqual(sieve_summary(10).primes, 4)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
