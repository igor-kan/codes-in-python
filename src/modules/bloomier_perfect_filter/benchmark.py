"""Microbenchmark runner for bloomier_perfect_filter."""

import time


def run_benchmark() -> float:
    from core import Xor16Filter
    from fast_path import batch_probe_count
    eng = Xor16Filter()
    flt = eng.build(list(range(1000)))
    qs = list(range(500))
    t0 = time.perf_counter()
    acc = 0
    for _ in range(50):
        acc += batch_probe_count(flt, qs)
    elapsed = (time.perf_counter() - t0) / 50.0
    print(f"bloomier_perfect_filter elapsed_ms={elapsed * 1000.0:.3f} acc={acc}")
    return elapsed


if __name__ == "__main__":
    run_benchmark()
