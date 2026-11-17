import unittest
from concurrency import parallel_restarts

class TestNmProps(unittest.TestCase):
    def test_quad_parallel(self):
        best = parallel_restarts(lambda x: (x[0]-3.0)**2 + (x[1]+2.0)**2, [[0.0,0.0], [5.0,5.0]])
        self.assertLess(best, 1e-5)

if __name__ == '__main__':
    unittest.main()
