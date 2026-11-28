from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

import hashlib

_MIN_PRECISION = 4
_MAX_PRECISION = 16


class HyperLogLog:
    def __init__(self, precision: int = 12) -> None:
        if precision < _MIN_PRECISION or precision > _MAX_PRECISION:
            raise ValidationError("precision must be between 4 and 16")
        self.precision = precision
        self.width = 1 << precision
        self.registers = [0] * self.width

    @staticmethod
    def _digest(item) -> int:
        raw = repr(item).encode("utf-8")
        return int.from_bytes(hashlib.blake2b(raw, digest_size=8).digest(), "big")

    def add(self, item) -> None:
        h = self._digest(item)
        index = h >> (64 - self.precision)
        rem_bits = 64 - self.precision
        w = h & ((1 << rem_bits) - 1)
        rank = rem_bits + 1 if w == 0 else rem_bits - w.bit_length() + 1
        if rank > self.registers[index]:
            self.registers[index] = rank

    def merge(self, other: "HyperLogLog") -> "HyperLogLog":
        if other.precision != self.precision:
            raise ValidationError("cannot merge sketches with different precision")
        out = HyperLogLog(self.precision)
        out.registers = [max(a, b) for a, b in zip(self.registers, other.registers)]
        return out

    def estimate(self) -> float:
        m = float(self.width)
        alpha = 0.7213 / (1.0 + 1.079 / m)
        inv_sum = sum(2.0 ** (-r) for r in self.registers)
        est = alpha * m * m / inv_sum
        if est <= 2.5 * m:
            zeros = self.registers.count(0)
            if zeros:
                est = m * math.log(m / zeros)
        return est

    def report(self) -> HllEstimate:
        return HllEstimate(estimate=self.estimate(), registers=self.width)
