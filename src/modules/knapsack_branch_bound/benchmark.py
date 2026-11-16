"""Microbenchmark runner for knapsack_branch_bound."""

import time


def run_benchmark() -> float:
    from core import BranchAndBoundKnapsack
    from models import KnapsackItem
    solver = BranchAndBoundKnapsack()
    items = [KnapsackItem(i, (i * 3) % 19 + 1, (i * 7) % 41 + 10) for i in range(18)]
    t0 = time.perf_counter()
    acc = 0
    for _ in range(50):
        acc += solver.solve(items, 85).optimal_value
    elapsed = (time.perf_counter() - t0) / 50.0
    print(f"knapsack_branch_bound elapsed_ms={elapsed * 1000.0:.3f} acc={acc}")
    return elapsed


if __name__ == "__main__":
    run_benchmark()
