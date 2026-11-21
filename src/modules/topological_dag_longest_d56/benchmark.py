import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += dag_longest_path(4, [(0, 1, 3), (1, 2, 4), (2, 3, 5)])[0]
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"topological_dag_longest_d56 ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
