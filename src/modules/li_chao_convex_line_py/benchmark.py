import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        lc = LiChaoTree(16); lc.add_line(2, 5); sink += lc.query(3)
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"li_chao_convex_line_py ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
