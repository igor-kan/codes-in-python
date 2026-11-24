import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        c = LfuCachePy(4); c.put(1, 5); sink += c.get(1)
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"lfu_cache_py_d59 ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
