import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        qt = QuadNode(0.0, 0.0, 50.0, 50.0, cap=2)
        for p in [(1.0,1.0),(2.0,2.0),(3.0,3.0),(4.0,4.0)]: qt.insert(p)
        sink += len(qt.query_box(0.0, 0.0, 10.0, 10.0))
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"quadtree_points_d58 ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
