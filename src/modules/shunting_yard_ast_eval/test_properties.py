import unittest
from concurrency import parallel_eval

class TestShuntingProps(unittest.TestCase):
    def test_batch(self):
        self.assertEqual(parallel_eval(['2*3+4', '2*(3+4)', '100-50/2']), [10, 14, 75])

if __name__ == '__main__':
    unittest.main()
