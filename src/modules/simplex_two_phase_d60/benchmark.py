import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += int(round(solve_lp_std([[1.0, 1.0], [2.0, 1.0]], [4.0, 6.0], [3.0, 2.0]).objective))
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"simplex_two_phase_d60 ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
