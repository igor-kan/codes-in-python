import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += int(detect_fx_arbitrage([[1.0, 2.0], [0.6, 1.0]]))
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"bellman_arbitrage_d58 ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
