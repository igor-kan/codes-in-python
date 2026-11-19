import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += hungarian_min_cost([[4,1,3],[2,0,5],[3,2,2]]).cost
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"hungarian_assign_o_n3_py ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
