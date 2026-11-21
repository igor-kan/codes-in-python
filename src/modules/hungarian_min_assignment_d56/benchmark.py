import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += hungarian_min_cost([[4, 2, 8], [4, 3, 7], [3, 1, 6]])[0]
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"hungarian_min_assignment_d56 ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
