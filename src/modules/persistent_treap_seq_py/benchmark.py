import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += pt_sum(pt_make(10, 1))
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"persistent_treap_seq_py ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
