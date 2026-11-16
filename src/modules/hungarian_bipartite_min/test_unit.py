from core import HungarianPotentialSolver
from fast_path import small_exact_oracle
from invariants import verify_assignment_feasible


def run_tests() -> None:
    mat = [
        [9.0, 2.0, 7.0, 8.0],
        [6.0, 4.0, 3.0, 7.0],
        [5.0, 8.0, 1.0, 8.0],
        [7.0, 6.0, 9.0, 4.0],
    ]
    res = HungarianPotentialSolver().solve_min_cost(mat)
    verify_assignment_feasible(mat, res)
    assert abs(res.total_cost - small_exact_oracle(mat)) < 1e-9
    assert abs(res.total_cost - 13.0) < 1e-9


if __name__ == "__main__":
    run_tests()
