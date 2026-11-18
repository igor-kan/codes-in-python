import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        r0 = None
        for i in range(1, 6):
            r0 = pt_merge(r0, pt_make(i * 10, (i * 2654435761) & 0xFFFFFFFF))
        a, b = pt_split(r0, 2)
        r1 = pt_merge(a, pt_merge(pt_make(99, 123456), b))
        self.assertEqual(pt_sum(r0), 150)
        self.assertEqual(pt_sum(r1), 249)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
