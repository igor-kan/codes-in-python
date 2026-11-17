import unittest
from concurrency import parallel_solve_rhs
from invariants import verify_residual

class TestPcgProps(unittest.TestCase):
    def test_parallel(self):
        a = [[10.0, 1.0], [1.0, 10.0]]
        rs = [[11.0, 11.0], [21.0, 12.0]]
        xs = parallel_solve_rhs(a, rs)
        for x, b in zip(xs, rs):
            verify_residual(a, x, b)

if __name__ == '__main__':
    unittest.main()
