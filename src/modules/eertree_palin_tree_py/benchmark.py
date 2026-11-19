import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += Eertree('abacaba').distinct_count()
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"eertree_palin_tree_py ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
