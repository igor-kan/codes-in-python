import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += query_rmq_idx(build_cartesian([9, 3, 7, 1, 5]), 0, 4)
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"cartesian_tree_rmq_py ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
