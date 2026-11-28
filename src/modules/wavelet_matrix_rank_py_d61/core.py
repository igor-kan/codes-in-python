from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

class WaveletMatrix:
    def __init__(self, data: List[int]) -> None:
        if not data:
            raise ValidationError("wavelet matrix requires at least one value")
        if any(v < 0 for v in data):
            raise ValidationError("wavelet matrix requires non-negative values")
        self.size = len(data)
        self.bits = max(1, max(data).bit_length())
        self.prefix: List[List[int]] = []
        self.zero_count: List[int] = []
        current = list(data)
        for level in range(self.bits - 1, -1, -1):
            pref = [0] * (len(current) + 1)
            zeros: List[int] = []
            ones: List[int] = []
            for i, value in enumerate(current):
                if (value >> level) & 1:
                    pref[i + 1] = pref[i]
                    ones.append(value)
                else:
                    pref[i + 1] = pref[i] + 1
                    zeros.append(value)
            self.prefix.append(pref)
            self.zero_count.append(len(zeros))
            current = zeros + ones
        self.ordered = current

    def rank(self, value: int, lo: int, hi: int) -> int:
        if value < 0 or value >= (1 << self.bits):
            return 0
        if not (0 <= lo <= hi <= self.size):
            raise ValidationError("range must satisfy 0 <= lo <= hi <= size")
        for level in range(self.bits):
            shift = self.bits - 1 - level
            pref = self.prefix[level]
            z = self.zero_count[level]
            zlo = pref[lo]
            zhi = pref[hi]
            if (value >> shift) & 1:
                lo = z + (lo - zlo)
                hi = z + (hi - zhi)
            else:
                lo = zlo
                hi = zhi
        return hi - lo

    def kth_smallest(self, k: int, lo: int, hi: int) -> int:
        if not (0 <= lo <= hi <= self.size):
            raise ValidationError("range must satisfy 0 <= lo <= hi <= size")
        if not (0 <= k < hi - lo):
            raise ValidationError("k must index inside the requested range")
        value = 0
        for level in range(self.bits):
            pref = self.prefix[level]
            z = self.zero_count[level]
            zlo = pref[lo]
            zhi = pref[hi]
            zeros = zhi - zlo
            if k < zeros:
                lo = zlo
                hi = zhi
            else:
                k -= zeros
                value |= 1 << (self.bits - 1 - level)
                lo = z + (lo - zlo)
                hi = z + (hi - zhi)
        return value
