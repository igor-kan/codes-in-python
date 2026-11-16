import cmath
import math
from typing import List, Sequence


def naive_dft(signal: Sequence[complex]) -> List[complex]:
    n = len(signal)
    out: List[complex] = []
    for k in range(n):
        acc = 0j
        for t in range(n):
            acc += signal[t] * cmath.exp(-2j * math.pi * k * t / n)
        out.append(acc)
    return out
