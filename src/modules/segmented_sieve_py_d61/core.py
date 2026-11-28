from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def _simple_primes(limit: int) -> List[int]:
    if limit < 2:
        return []
    flags = [True] * (limit + 1)
    flags[0] = False
    flags[1] = False
    for p in range(2, math.isqrt(limit) + 1):
        if flags[p]:
            for multiple in range(p * p, limit + 1, p):
                flags[multiple] = False
    return [i for i, is_prime in enumerate(flags) if is_prime]


def segmented_primes(limit: int) -> List[int]:
    if limit < 0:
        raise ValidationError("limit must be non-negative")
    if limit < 2:
        return []
    root = math.isqrt(limit)
    base = _simple_primes(root)
    primes = list(base)
    window = 1 << 15
    low = root + 1
    while low <= limit:
        high = min(low + window - 1, limit)
        size = high - low + 1
        flags = bytearray([1]) * size
        for p in base:
            start = max(p * p, ((low + p - 1) // p) * p)
            for multiple in range(start, high + 1, p):
                flags[multiple - low] = 0
        for offset in range(size):
            if flags[offset]:
                primes.append(low + offset)
        low = high + 1
    return primes


def prime_pi(limit: int) -> int:
    return len(segmented_primes(limit))


def sieve_summary(limit: int) -> SieveSummary:
    return SieveSummary(limit=limit, primes=prime_pi(limit))
