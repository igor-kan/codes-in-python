"""Microbenchmark runner for kd_tree_nearest_py."""

import time


def run_benchmark() -> float:
    from core import KdTreeIndex
    pts = [((i * 19) % 101, (i * 31) % 97, (i * 13) % 89) for i in range(400)]
    kd = KdTreeIndex(pts)
    t0 = time.perf_counter()
    acc = 0
    for _ in range(50):
        acc += len(kd.k_nearest((25.0, 30.0, 40.0), 5))
    elapsed = (time.perf_counter() - t0) / 50.0
    print(f"kd_tree_nearest_py elapsed_ms={elapsed * 1000.0:.3f} acc={acc}")
    return elapsed


if __name__ == "__main__":
    run_benchmark()
