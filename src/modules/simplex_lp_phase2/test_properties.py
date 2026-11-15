import random
import unittest
from core import BlandSimplexSolver
from invariants import verify_primal_feasibility
from models import LinearProgram


class TestSimplexRandomized(unittest.TestCase):
    def test_positive_resource_lps(self) -> None:
        rng = random.Random(88)
        solver = BlandSimplexSolver()
        for _ in range(15):
            a_rows = tuple(tuple(float(rng.randint(1, 5)) for _ in range(4)) for _ in range(4))
            c = tuple(float(rng.randint(1, 10)) for _ in range(4))
            b = tuple(float(rng.randint(10, 40)) for _ in range(4))
            lp = LinearProgram(c=c, a_rows=a_rows, b=b)
            sol = solver.maximize(lp)
            verify_primal_feasibility(lp, sol)


if __name__ == "__main__":
    unittest.main()
