import time
from core import EarleyParser

def run_benchmark() -> None:
    p=EarleyParser({'E':[('E','+','x'),('x',)]}, 'E'); toks=list('x+'*12 + 'x')
    t0 = time.perf_counter_ns()
    sink = 0.0
    for it in range(200):
        sink += 1 if p.recognizes(toks) else 0
    elapsed_ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"earley_cfg_parser ms={elapsed_ms:.3f} sink={sink:.3f}")


if __name__ == "__main__":
    run_benchmark()
