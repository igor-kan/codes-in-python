import unittest
from core import *
from validation import require_positive
from invariants import ensure_postcondition

class TestUnit(unittest.TestCase):
    def test_core(self) -> None:
        require_positive(1)
        self.assertEqual(longest_palindrome("babad"), PalindromeSpan(0, 3))
        self.assertEqual(longest_palindrome("cbbd"), PalindromeSpan(1, 2))
        self.assertEqual(longest_palindrome(""), PalindromeSpan(0, 0))
        self.assertEqual(longest_palindrome("racecar"), PalindromeSpan(0, 7))
        ensure_postcondition(True)

if __name__ == "__main__":
    unittest.main()
