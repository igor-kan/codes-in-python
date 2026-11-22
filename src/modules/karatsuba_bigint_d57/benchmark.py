import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += karatsuba_mul(123456789, 987654321)
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"karatsuba_bigint_d57 ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
