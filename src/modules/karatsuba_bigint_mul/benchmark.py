import time
from core import KaratsubaMultiplier, from_int


def main() -> None:
    a = from_int(10 ** 800 - 1)
    b = from_int(10 ** 800 - 17)
    mul = KaratsubaMultiplier()
    t0 = time.perf_counter_ns()
    p = mul.multiply(a, b)
    elapsed = (time.perf_counter_ns() - t0) / 1e6
    assert len(p.limbs) > 0
    print(f"karatsuba_bigint_mul: {elapsed:.3f} ms limbs={len(p.limbs)}")


if __name__ == "__main__":
    main()
