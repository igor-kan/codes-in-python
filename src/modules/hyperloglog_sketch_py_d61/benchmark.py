import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        h = HyperLogLog(8)
        for j in range(20):
            h.add(j)
        sink += int(h.estimate())
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"hyperloglog_sketch_py_d61 ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
