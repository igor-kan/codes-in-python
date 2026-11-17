import time
from models import WeightedItem
from core import ares_sample

def run_benchmark() -> None:
    items=[WeightedItem(i, float(i+1)) for i in range(100)]
    t0 = time.perf_counter_ns()
    sink = 0.0
    for it in range(200):
        sink += len(ares_sample(items, 10, seed=it + 1))
    elapsed_ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"reservoir_weighted_chao ms={elapsed_ms:.3f} sink={sink:.3f}")


if __name__ == "__main__":
    run_benchmark()
