import random
from concurrency import batch_solve_assignments
from fast_path import small_exact_oracle
from invariants import verify_assignment_feasible


def run_properties() -> None:
    rng = random.Random(77)
    mats = [[[rng.uniform(-20.0, 50.0) for _ in range(6)] for _ in range(5)] for _ in range(8)]
    results = batch_solve_assignments(mats)
    for mat, res in zip(mats, results):
        verify_assignment_feasible(mat, res)
        oracle = small_exact_oracle(mat)
        assert abs(res.total_cost - oracle) < 1e-7


if __name__ == "__main__":
    run_properties()
