import unittest
from core import nelder_mead
from fast_path import rosenbrock
from invariants import verify_converged

class TestNm(unittest.TestCase):
    def test_rosenbrock_2d(self):
        res = nelder_mead(rosenbrock, [0.0, 0.0], max_iter=1000, tol=1e-10)
        verify_converged(res, 1e-4)

if __name__ == '__main__':
    unittest.main()
