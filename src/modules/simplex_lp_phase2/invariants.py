import math
from models import LinearProgram, SimplexSolution


def verify_primal_feasibility(lp: LinearProgram, sol: SimplexSolution) -> None:
    assert sol.status == "OPTIMAL"
    for xj in sol.primal_x:
        assert xj >= -1e-9
    for row, rhs in zip(lp.a_rows, lp.b):
        lhs = sum(a * x for a, x in zip(row, sol.primal_x))
        assert lhs <= rhs + 1e-8
    obj = sum(c * x for c, x in zip(lp.c, sol.primal_x))
    assert math.isclose(obj, sol.objective_value, abs_tol=1e-8)
