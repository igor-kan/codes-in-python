import unittest
from core import BlandSimplexSolver
from invariants import verify_primal_feasibility
from models import LinearProgram
from validation import validate_lp


class TestSimplexSolver(unittest.TestCase):
    def test_classic_2var_lp(self) -> None:
        lp = LinearProgram(
            c=(3.0, 5.0),
            a_rows=((1.0, 0.0), (0.0, 2.0), (3.0, 2.0)),
            b=(4.0, 12.0, 18.0),
        )
        validate_lp(lp)
        sol = BlandSimplexSolver().maximize(lp)
        verify_primal_feasibility(lp, sol)
        self.assertAlmostEqual(sol.objective_value, 36.0, places=9)
        self.assertAlmostEqual(sol.primal_x[0], 2.0, places=9)
        self.assertAlmostEqual(sol.primal_x[1], 6.0, places=9)


if __name__ == "__main__":
    unittest.main()
