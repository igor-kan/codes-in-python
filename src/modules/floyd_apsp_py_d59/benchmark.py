import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += int(floyd_apsp([[0.0, 4.0, 9.0], [2.0, 0.0, 1.0], [8.0, 3.0, 0.0]])[1][0][2])
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"floyd_apsp_py_d59 ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
