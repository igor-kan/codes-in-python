import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += hopcroft_karp(2, 2, [(0,0),(0,1),(1,0)]).size
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"hopcroft_karp_bipartite_py ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
