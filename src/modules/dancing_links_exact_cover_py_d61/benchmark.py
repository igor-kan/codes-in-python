import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += len(exact_cover([[0, 1], [2, 3], [4, 5], [6, 7], [0, 2], [1, 3], [4, 6], [5, 7]], 8, limit=4).solutions)
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"dancing_links_exact_cover_py_d61 ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
