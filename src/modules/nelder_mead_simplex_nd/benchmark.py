import time
from core import nelder_mead

def run_benchmark() -> None:
    quad=lambda v: sum((x-1.0)**2 for x in v)
    t0 = time.perf_counter_ns()
    sink = 0.0
    for it in range(200):
        sink += nelder_mead(quad, [0.0, 0.0], 80).fval
    elapsed_ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"nelder_mead_simplex_nd ms={elapsed_ms:.3f} sink={sink:.3f}")


if __name__ == "__main__":
    run_benchmark()
