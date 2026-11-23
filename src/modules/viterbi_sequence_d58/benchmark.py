import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += sum(viterbi_log_path([0.6, 0.4], [[0.7, 0.3], [0.4, 0.6]], [[0.8, 0.2], [0.2, 0.8]], [0, 1, 0])[0])
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"viterbi_sequence_d58 ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
