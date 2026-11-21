import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        msg = "abracadabra"
        self.assertEqual(huffman_roundtrip(msg), msg)
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
