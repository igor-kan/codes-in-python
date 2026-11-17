import unittest
from core import EarleyParser
from invariants import verify_grammar_language

class TestEarley(unittest.TestCase):
    def test_left_recursive_arith(self):
        g = {'E': [('E', '+', 'T'), ('T',)], 'T': [('T', '*', 'F'), ('F',)], 'F': [('(', 'E', ')'), ('x',)]}
        p = EarleyParser(g, 'E')
        verify_grammar_language(p, [list('x+x*x'), list('(x+x)*x')], [list('x++x'), list('(x')])

if __name__ == '__main__':
    unittest.main()
