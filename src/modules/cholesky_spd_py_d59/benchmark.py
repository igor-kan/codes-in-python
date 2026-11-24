import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += int(cholesky_lower([[4.0, 2.0], [2.0, 5.0]])[1][1] * 100)
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"cholesky_spd_py_d59 ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
