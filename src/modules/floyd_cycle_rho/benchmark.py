import time
from fast_path import brent_detect


def main() -> None:
    fn = lambda x: (1664525 * x + 1013904223) & 0xFFFF
    t0 = time.perf_counter_ns()
    sig = brent_detect(fn, 42)
    elapsed = (time.perf_counter_ns() - t0) / 1e6
    assert sig.period_length == 65536
    print(f"floyd_cycle_rho: {elapsed:.3f} ms period={sig.period_length}")


if __name__ == "__main__":
    main()
