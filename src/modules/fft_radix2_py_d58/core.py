from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

import cmath

def dft_rad2(xs: List[complex]) -> List[complex]:
    n = len(xs)
    if n <= 1:
        return list(xs)
    even = dft_rad2(xs[0::2])
    odd = dft_rad2(xs[1::2])
    half = n // 2
    out = [0j] * n
    for k in range(half):
        w = cmath.exp(-2j * cmath.pi * k / n) * odd[k]
        out[k] = even[k] + w
        out[k + half] = even[k] - w
    return out

def idft_rad2(freq: List[complex]) -> List[complex]:
    n = len(freq)
    conj = [v.conjugate() for v in freq]
    inv = dft_rad2(conj)
    return [v.conjugate() / n for v in inv]
