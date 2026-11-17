import unittest
from core import solve_pcg
from invariants import verify_residual

class TestPcg(unittest.TestCase):
    def test_tridiag_spd(self):
        a = [[4.0,-1.0,0.0],[-1.0,4.0,-1.0],[0.0,-1.0,4.0]]
        b = [15.0, 10.0, 10.0]
        sol = solve_pcg(a, b)
        verify_residual(a, sol.x, b)

if __name__ == '__main__':
    unittest.main()
