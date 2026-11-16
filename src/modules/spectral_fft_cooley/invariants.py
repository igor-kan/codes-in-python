from typing import Sequence
from core import CooleyTukeyFFT
from exceptions import FftDomainError
from fast_path import naive_dft


def verify_parseval_and_roundtrip(signal: Sequence[complex]) -> None:
    eng = CooleyTukeyFFT()
    spec = eng.forward(signal)
    if abs(spec.time_energy - spec.freq_energy) > 1e-8 * max(1.0, spec.time_energy):
        raise FftDomainError("Parseval energy mismatch")
    rec = eng.inverse(spec.bins)
    for a, b in zip(signal, rec):
        if abs(a - b) > 1e-9:
            raise FftDomainError("IFFT roundtrip residual exceeded tolerance")
    if len(signal) <= 64:
        oracle = naive_dft(signal)
        for a, b in zip(spec.bins, oracle):
            if abs(a - b) > 1e-9:
                raise FftDomainError("FFT vs DFT oracle mismatch")
