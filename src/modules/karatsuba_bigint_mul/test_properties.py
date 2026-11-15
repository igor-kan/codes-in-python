import random
import unittest
from core import KaratsubaMultiplier, from_int
from invariants import verify_product


class TestKaratsubaProperties(unittest.TestCase):
    def test_commutativity_and_oracle(self) -> None:
        rng = random.Random(4242)
        mul = KaratsubaMultiplier()
        for _ in range(25):
            a_val = rng.getrandbits(400) * (1 if rng.random() > 0.5 else -1)
            b_val = rng.getrandbits(350) * (1 if rng.random() > 0.5 else -1)
            a = from_int(a_val)
            b = from_int(b_val)
            p1 = mul.multiply(a, b)
            p2 = mul.multiply(b, a)
            verify_product(a, b, p1)
            self.assertEqual(p1, p2)


if __name__ == "__main__":
    unittest.main()
