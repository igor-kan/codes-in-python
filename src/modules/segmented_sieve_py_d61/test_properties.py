import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        def trial_prime(n: int) -> bool:
            if n < 2:
                return False
            d = 2
            while d * d <= n:
                if n % d == 0:
                    return False
                d += 1
            return True
        for limit in (0, 1, 2, 10, 97, 200):
            self.assertEqual(segmented_primes(limit), [n for n in range(2, limit + 1) if trial_prime(n)])
        self.assertEqual(prime_pi(10 ** 6), 78498)

if __name__ == "__main__":
    unittest.main()
