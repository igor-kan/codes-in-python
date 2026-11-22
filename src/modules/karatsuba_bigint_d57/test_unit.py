import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        a = 1234567890123456789
        b = 9876543210987654321
        self.assertEqual(karatsuba_mul(a, b), a * b)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
