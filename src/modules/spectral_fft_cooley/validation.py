import math
from typing import Sequence
from exceptions import FftDimensionError, FftDomainError


def validate_fft_input(seq: Sequence[complex]) -> None:
    n = len(seq)
    if n == 0 or (n & (n - 1)) != 0:
        raise FftDimensionError(f"FFT length must be non-zero power of two, got {n}")
    for z in seq:
        if not (math.isfinite(z.real) and math.isfinite(z.imag)):
            raise FftDomainError("non-finite complex component")
