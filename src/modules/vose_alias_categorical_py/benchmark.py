import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        t = build_alias_table([1.0, 2.0, 3.0]); sink += sample_alias(t, 1, 0.5)
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"vose_alias_categorical_py ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
