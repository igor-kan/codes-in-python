import random
from concurrency import batch_forward_fft
from invariants import verify_parseval_and_roundtrip


def run_properties() -> None:
    rng = random.Random(101)
    sigs = [[complex(rng.uniform(-5, 5), rng.uniform(-5, 5)) for _ in range(64)] for _ in range(6)]
    for s in sigs:
        verify_parseval_and_roundtrip(s)
    specs = batch_forward_fft(sigs)
    assert all(abs(sp.time_energy - sp.freq_energy) < 1e-7 for sp in specs)


if __name__ == "__main__":
    run_properties()
