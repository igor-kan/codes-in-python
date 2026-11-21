import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += int(earley_accepts({"S": [("a", "S", "b"), ("a", "b")]}, "S", ["a", "a", "b", "b"]))
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"earley_cfg_recogniser_d56 ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
