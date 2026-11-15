import time
from core import BlandSimplexSolver
from models import LinearProgram


def main() -> None:
    n = 16
    a_rows = tuple(tuple(1.0 if i == j else 0.1 for j in range(n)) for i in range(n))
    c = tuple(float(i + 1) for i in range(n))
    b = tuple(10.0 for _ in range(n))
    lp = LinearProgram(c=c, a_rows=a_rows, b=b)
    t0 = time.perf_counter_ns()
    sol = BlandSimplexSolver().maximize(lp)
    elapsed = (time.perf_counter_ns() - t0) / 1e6
    assert sol.status == "OPTIMAL"
    print(f"simplex_lp_phase2: {elapsed:.3f} ms obj={sol.objective_value:.2f}")


if __name__ == "__main__":
    main()
