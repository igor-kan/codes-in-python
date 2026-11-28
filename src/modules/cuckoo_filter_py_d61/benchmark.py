import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        f = CuckooFilter(capacity=64, bucket_size=4)
        for j in range(16):
            f.insert(j)
        sink += f.count
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"cuckoo_filter_py_d61 ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
