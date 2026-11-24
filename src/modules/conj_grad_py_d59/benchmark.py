import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += int(cg_solve([[4.0, 1.0], [1.0, 3.0]], [1.0, 2.0])[0] * 1000)
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"conj_grad_py_d59 ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
