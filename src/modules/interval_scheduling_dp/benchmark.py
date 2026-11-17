import time
from models import JobInterval
from core import solve_weighted_intervals

def run_benchmark() -> None:
    jobs=[JobInterval(i, i+3, (i*7)%11 + 1) for i in range(64)]
    t0 = time.perf_counter_ns()
    sink = 0.0
    for it in range(200):
        sink += solve_weighted_intervals(jobs)[0]
    elapsed_ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"interval_scheduling_dp ms={elapsed_ms:.3f} sink={sink:.3f}")


if __name__ == "__main__":
    run_benchmark()
