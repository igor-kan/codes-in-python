import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += solve_blossom_matching(4, [(0,1),(1,2),(2,0),(2,3)]).pairs
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"edmonds_blossom_general_py ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
