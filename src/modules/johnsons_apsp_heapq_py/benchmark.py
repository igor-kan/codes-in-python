import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += johnson_apsp(3, [(0,1,4),(1,2,-2)]).dist[0][2]
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"johnsons_apsp_heapq_py ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
