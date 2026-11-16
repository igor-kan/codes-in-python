"""Microbenchmark runner for hungarian_bipartite_min."""

import time


def run_benchmark() -> float:
    from core import HungarianPotentialSolver
    solver = HungarianPotentialSolver()
    mat = [[float((i * 7 + j * 13) % 97) for j in range(24)] for i in range(24)]
    t0 = time.perf_counter()
    acc = 0
    for _ in range(50):
        acc += int(solver.solve_min_cost(mat).total_cost)
    elapsed = (time.perf_counter() - t0) / 50.0
    print(f"hungarian_bipartite_min elapsed_ms={elapsed * 1000.0:.3f} acc={acc}")
    return elapsed


if __name__ == "__main__":
    run_benchmark()
