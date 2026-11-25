import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += edit_cost(hirschberg_align("algorithm", "altruistic"))
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"edit_distance_hirschberg_d60 ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
