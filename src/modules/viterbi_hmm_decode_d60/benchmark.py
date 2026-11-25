import time
from core import *

def run_benchmark() -> None:
    t0 = time.perf_counter_ns()
    sink = 0
    for it in range(100):
        sink += sum(viterbi_decode([0, 1, 2], [0.6, 0.4], [[0.7, 0.3], [0.4, 0.6]], [[0.5, 0.4, 0.1], [0.1, 0.3, 0.6]]).states)
    ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"viterbi_hmm_decode_d60 ms={ms:.3f} sink={sink}")

if __name__ == "__main__":
    run_benchmark()
