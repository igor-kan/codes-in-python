import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += int(pagerank_scores(4, [(0, 1), (1, 2), (2, 3), (3, 0)], iters=10)[0] * 1000)
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"pagerank_power_iter_d56 ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
