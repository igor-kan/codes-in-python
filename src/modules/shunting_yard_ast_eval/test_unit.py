import unittest
from invariants import verify_against_expected

class TestShuntingYard(unittest.TestCase):
    def test_precedence_and_parens(self):
        verify_against_expected('3 + 4 * 2 / (1 - 5) + 10', 11)
        verify_against_expected('(12 + 8) * (7 - 2)', 100)

if __name__ == '__main__':
    unittest.main()
