import time
from core import align_hirschberg

def run_benchmark() -> None:
    a='abacaba'*4; b='abdbaba'*4
    t0 = time.perf_counter_ns()
    sink = 0.0
    for it in range(200):
        sink += align_hirschberg(a, b).distance
    elapsed_ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"levenshtein_hirschberg_linear ms={elapsed_ms:.3f} sink={sink:.3f}")


if __name__ == "__main__":
    run_benchmark()
