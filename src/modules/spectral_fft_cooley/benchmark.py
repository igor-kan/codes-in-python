"""Microbenchmark runner for spectral_fft_cooley."""

import time


def run_benchmark() -> float:
    from core import CooleyTukeyFFT
    eng = CooleyTukeyFFT()
    sig = [complex(i & 7, (i * 3) & 3) for i in range(256)]
    t0 = time.perf_counter()
    acc = 0
    for _ in range(50):
        acc += len(eng.forward(sig).bins)
    elapsed = (time.perf_counter() - t0) / 50.0
    print(f"spectral_fft_cooley elapsed_ms={elapsed * 1000.0:.3f} acc={acc}")
    return elapsed


if __name__ == "__main__":
    run_benchmark()
