import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        tree = build_kd_tree([(1.0, 1.0), (4.0, 5.0), (8.0, 2.0), (3.0, 9.0)])
        sink += int(kd_nearest(tree, (2.0, 2.0))[0][0])
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"kd_tree_nearest_py_d60 ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
