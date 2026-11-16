"""Microbenchmark runner for tarjan_scc_dag_py."""

import time


def run_benchmark() -> float:
    from core import IterativeTarjanSCC
    eng = IterativeTarjanSCC()
    edges = [(i, (i + 1) % 256) for i in range(256)] + [(i, (i + 7) % 256) for i in range(0, 256, 4)]
    t0 = time.perf_counter()
    acc = 0
    for _ in range(50):
        acc += len(eng.decompose(256, edges).components)
    elapsed = (time.perf_counter() - t0) / 50.0
    print(f"tarjan_scc_dag_py elapsed_ms={elapsed * 1000.0:.3f} acc={acc}")
    return elapsed


if __name__ == "__main__":
    run_benchmark()
