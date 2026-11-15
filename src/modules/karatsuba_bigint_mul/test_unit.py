import unittest
from core import KaratsubaMultiplier, from_int, to_int
from fast_path import fast_square_int
from invariants import verify_product
from validation import validate_limbs


class TestKaratsuba(unittest.TestCase):
    def test_large_operands(self) -> None:
        a_val = (10 ** 120) - 987654321
        b_val = -((10 ** 110) + 123456789)
        a = from_int(a_val)
        b = from_int(b_val)
        validate_limbs(a)
        validate_limbs(b)
        prod = KaratsubaMultiplier().multiply(a, b)
        verify_product(a, b, prod)
        self.assertEqual(to_int(prod), a_val * b_val)
        self.assertEqual(fast_square_int(10 ** 80 + 7), (10 ** 80 + 7) ** 2)


if __name__ == "__main__":
    unittest.main()
