import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += min_cost_flow(4, 0, 3, [(0, 1, 2, 1), (0, 2, 2, 5), (1, 3, 2, 1), (2, 3, 2, 5)]).cost
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"min_cost_flow_spfa_py_d61 ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
