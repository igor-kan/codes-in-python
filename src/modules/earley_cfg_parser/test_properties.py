import unittest
from concurrency import parallel_recognize

class TestEarleyProps(unittest.TestCase):
    def test_nullable_parens(self):
        g = {'S': [('(', 'S', ')', 'S'), ()]}
        self.assertEqual(parallel_recognize(g, 'S', [list(''), list('(())()'), list('(()')]), [True, True, False])

if __name__ == '__main__':
    unittest.main()
