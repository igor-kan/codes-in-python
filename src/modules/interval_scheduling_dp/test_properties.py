import unittest
from models import JobInterval
from concurrency import parallel_best_weights

class TestWisProps(unittest.TestCase):
    def test_parallel(self):
        b1 = [JobInterval(0, 4, 10), JobInterval(1, 2, 6), JobInterval(3, 4, 6)]
        b2 = [JobInterval(0, 5, 100)]
        self.assertEqual(parallel_best_weights([b1, b2]), [12, 100])

if __name__ == '__main__':
    unittest.main()
