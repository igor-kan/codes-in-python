import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += astar_grid_steps([[0, 0, 0], [0, 1, 0], [0, 0, 0]], (0, 0), (2, 2))
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"astar_manhattan_grid_d57 ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
