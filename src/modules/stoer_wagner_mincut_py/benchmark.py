import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += stoer_wagner_mincut(3, [[0,3,1],[3,0,2],[1,2,0]]).weight
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"stoer_wagner_mincut_py ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
