import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        sig = [1.0 + 0j, 2.0 + 0j, 3.0 + 0j, 4.0 + 0j]
        rec = idft_rad2(dft_rad2(sig))
        for a, b in zip(sig, rec):
            self.assertAlmostEqual(a.real, b.real, places=9)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
