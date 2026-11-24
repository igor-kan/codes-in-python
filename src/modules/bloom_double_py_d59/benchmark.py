import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        bf = IntBitBloom(); bf.add(77); sink += int(bf.might_contain(77))
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"bloom_double_py_d59 ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
