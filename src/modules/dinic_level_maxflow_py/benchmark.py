import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += dinic_max_flow(3, 0, 2, [(0,1,5),(1,2,5)])
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"dinic_level_maxflow_py ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
