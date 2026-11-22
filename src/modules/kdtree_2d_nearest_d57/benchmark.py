import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += int(kdtree_nearest_sq(build_kdtree([(1.0, 2.0), (4.0, 6.0)]), (2.0, 3.0)) * 100)
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"kdtree_2d_nearest_d57 ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
