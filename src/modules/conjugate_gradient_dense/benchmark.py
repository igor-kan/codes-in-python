import time
from core import solve_pcg

def run_benchmark() -> None:
    a=[[4.0 if i==j else (-1.0 if abs(i-j)==1 else 0.0) for j in range(12)] for i in range(12)]; b=[1.0]*12
    t0 = time.perf_counter_ns()
    sink = 0.0
    for it in range(200):
        sink += solve_pcg(a, b).x[0]
    elapsed_ms = (time.perf_counter_ns() - t0) / 1e6
    print(f"conjugate_gradient_dense ms={elapsed_ms:.3f} sink={sink:.3f}")


if __name__ == "__main__":
    run_benchmark()
