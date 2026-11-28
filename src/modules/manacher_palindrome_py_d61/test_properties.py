import unittest
from core import *
from concurrency import parallel_fold_batches

class TestProperties(unittest.TestCase):
    def test_properties(self) -> None:
        chks = parallel_fold_batches([[1, 2], [3, 4]])
        self.assertEqual(len(chks), 2)
        def brute(s: str) -> PalindromeSpan:
            best = PalindromeSpan(0, 0)
            for i in range(len(s)):
                for j in range(i + 1, len(s) + 1):
                    piece = s[i:j]
                    if piece == piece[::-1] and j - i > best.length:
                        best = PalindromeSpan(i, j - i)
            return best
        samples = ["a", "aa", "ab", "forgeeksskeegfor", "abacdfgdcaba", "xyzzy", "aabbaa"]
        for text in samples:
            got = longest_palindrome(text)
            want = brute(text)
            self.assertEqual(got.length, want.length)
            piece = text[got.start:got.start + got.length]
            self.assertEqual(piece, piece[::-1])

if __name__ == "__main__":
    unittest.main()
