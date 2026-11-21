import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        tr = DeterministicTreap()
        for x in [5, 2, 8, 1]: tr.insert(x)
        sink += tr.kth(2)
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"splay_treap_split_merge_d56 ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
