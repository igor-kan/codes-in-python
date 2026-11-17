import time
from core import analyze_dag

def run_benchmark() -> None:
    edges=[(i, i+1) for i in range(63)] + [(i, i+2) for i in range(62)]
    t0 = time.perf_counter_ns()
    sink = 0.0
    for it in range(200):
        sink += analyze_dag(64, edges, 0).path_counts[-1]
    elapsed_ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"topological_sort_all_paths ms={elapsed_ms:.3f} sink={sink:.3f}")


if __name__ == "__main__":
    run_benchmark()
