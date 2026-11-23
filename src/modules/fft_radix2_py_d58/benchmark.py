import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += int(abs(dft_rad2([1+0j, 2+0j, 3+0j, 4+0j])[0]))
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"fft_radix2_py_d58 ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
