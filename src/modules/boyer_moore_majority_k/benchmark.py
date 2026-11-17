import time
from core import misra_gries_heavy

def run_benchmark() -> None:
    s=[i % 17 for i in range(512)] + [99]*200
    t0 = time.perf_counter_ns()
    sink = 0.0
    for it in range(200):
        sink += len(misra_gries_heavy(s, 4).verified_counts)
    elapsed_ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"boyer_moore_majority_k ms={elapsed_ms:.3f} sink={sink:.3f}")


if __name__ == "__main__":
    run_benchmark()
