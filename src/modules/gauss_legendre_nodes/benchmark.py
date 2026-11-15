import math
import time
from core import GaussLegendreEngine


def main() -> None:
    eng = GaussLegendreEngine()
    t0 = time.perf_counter_ns()
    rule = eng.generate_rule(64)
    val = eng.integrate(rule, math.cos, 0.0, 1.5)
    elapsed = (time.perf_counter_ns() - t0) / 1e6
    assert abs(val - math.sin(1.5)) < 1e-13
    print(f"gauss_legendre_nodes: {elapsed:.3f} ms val={val:.12f}")


if __name__ == "__main__":
    main()
