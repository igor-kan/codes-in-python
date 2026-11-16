import math
from invariants import verify_parseval_and_roundtrip


def run_tests() -> None:
    sig = [complex(math.cos(2 * math.pi * 3 * t / 32), math.sin(2 * math.pi * 5 * t / 32)) for t in range(32)]
    verify_parseval_and_roundtrip(sig)


if __name__ == "__main__":
    run_tests()
