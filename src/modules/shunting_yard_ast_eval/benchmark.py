import time
from fast_path import compile_and_eval

def run_benchmark() -> None:
    expr='(12 + 34) * 5 - 8 / 2 + 17'
    t0 = time.perf_counter_ns()
    sink = 0.0
    for it in range(200):
        sink += compile_and_eval(expr)
    elapsed_ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"shunting_yard_ast_eval ms={elapsed_ms:.3f} sink={sink:.3f}")


if __name__ == "__main__":
    run_benchmark()
