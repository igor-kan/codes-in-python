import cmath
import math
from typing import List, Sequence
from models import SpectrumResult
from validation import validate_fft_input


def _fft_core(buf: List[complex], invert: bool) -> List[complex]:
    n = len(buf)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            buf[i], buf[j] = buf[j], buf[i]

    length = 2
    sign = 1.0 if invert else -1.0
    while length <= n:
        ang = sign * 2.0 * math.pi / length
        wlen = cmath.rect(1.0, ang)
        half = length >> 1
        for start in range(0, n, length):
            w = 1.0 + 0.0j
            for k in range(half):
                u = buf[start + k]
                v = buf[start + k + half] * w
                buf[start + k] = u + v
                buf[start + k + half] = u - v
                w *= wlen
        length <<= 1

    if invert:
        inv_n = 1.0 / n
        for i in range(n):
            buf[i] *= inv_n
    return buf


class CooleyTukeyFFT:
    def forward(self, signal: Sequence[complex]) -> SpectrumResult:
        validate_fft_input(signal)
        work = [complex(z) for z in signal]
        t_energy = sum((z.real * z.real + z.imag * z.imag) for z in work)
        bins = _fft_core(work, False)
        f_energy = sum((z.real * z.real + z.imag * z.imag) for z in bins) / len(bins)
        return SpectrumResult(tuple(bins), t_energy, f_energy)

    def inverse(self, spectrum: Sequence[complex]) -> List[complex]:
        validate_fft_input(spectrum)
        return _fft_core([complex(z) for z in spectrum], True)
