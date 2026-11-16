"""Microbenchmark runner for pagerank_power_iter."""

import time


def run_benchmark() -> float:
    from core import SparsePageRank
    pr = SparsePageRank()
    edges = [(i, (i * 7 + 1) % 128) for i in range(128)] + [(i, (i * 11 + 3) % 128) for i in range(128)]
    t0 = time.perf_counter()
    acc = 0
    for _ in range(50):
        acc += pr.compute(128, edges, tol=1e-7).iterations
    elapsed = (time.perf_counter() - t0) / 50.0
    print(f"pagerank_power_iter elapsed_ms={elapsed * 1000.0:.3f} acc={acc}")
    return elapsed


if __name__ == "__main__":
    run_benchmark()
