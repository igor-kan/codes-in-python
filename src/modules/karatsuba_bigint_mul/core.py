from typing import List
from models import LIMB_BASE, LimbBigInt


def from_int(value: int) -> LimbBigInt:
    if value == 0:
        return LimbBigInt(limbs=(), negative=False)
    neg = value < 0
    v = -value if neg else value
    out: List[int] = []
    while v > 0:
        out.append(v % LIMB_BASE)
        v //= LIMB_BASE
    return LimbBigInt(limbs=tuple(out), negative=neg)


def to_int(num: LimbBigInt) -> int:
    acc = 0
    for limb in reversed(num.limbs):
        acc = acc * LIMB_BASE + limb
    return -acc if num.negative and acc > 0 else acc


def _trim(limbs: List[int]) -> List[int]:
    while limbs and limbs[-1] == 0:
        limbs.pop()
    return limbs


def _add_abs(a: List[int], b: List[int]) -> List[int]:
    n = max(len(a), len(b))
    out = [0] * (n + 1)
    carry = 0
    for i in range(n):
        s = carry + (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
        out[i] = s % LIMB_BASE
        carry = s // LIMB_BASE
    if carry:
        out[n] = carry
    return _trim(out)


def _sub_abs(a: List[int], b: List[int]) -> List[int]:
    out = [0] * len(a)
    borrow = 0
    for i in range(len(a)):
        diff = a[i] - borrow - (b[i] if i < len(b) else 0)
        if diff < 0:
            diff += LIMB_BASE
            borrow = 1
        else:
            borrow = 0
        out[i] = diff
    return _trim(out)


def _schoolbook(a: List[int], b: List[int]) -> List[int]:
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b))
    for i, ai in enumerate(a):
        carry = 0
        for j, bj in enumerate(b):
            cur = out[i + j] + ai * bj + carry
            out[i + j] = cur % LIMB_BASE
            carry = cur // LIMB_BASE
        out[i + len(b)] += carry
    return _trim(out)


def _karatsuba_abs(a: List[int], b: List[int]) -> List[int]:
    if len(a) <= 16 or len(b) <= 16:
        return _schoolbook(a, b)
    m = max(len(a), len(b)) // 2
    a_lo, a_hi = a[:m], a[m:]
    b_lo, b_hi = b[:m], b[m:]
    z0 = _karatsuba_abs(a_lo, b_lo)
    z2 = _karatsuba_abs(a_hi, b_hi)
    z1_sum = _karatsuba_abs(_add_abs(a_lo, a_hi), _add_abs(b_lo, b_hi))
    mid = _sub_abs(_sub_abs(z1_sum, z2), z0)
    res = [0] * (max(len(z0), len(mid) + m, len(z2) + 2 * m) + 1)
    for i, v in enumerate(z0):
        res[i] += v
    for i, v in enumerate(mid):
        res[i + m] += v
    for i, v in enumerate(z2):
        res[i + 2 * m] += v
    carry = 0
    for i in range(len(res)):
        v = res[i] + carry
        res[i] = v % LIMB_BASE
        carry = v // LIMB_BASE
    return _trim(res)


class KaratsubaMultiplier:
    def multiply(self, a: LimbBigInt, b: LimbBigInt) -> LimbBigInt:
        prod = _karatsuba_abs(list(a.limbs), list(b.limbs))
        if not prod:
            return LimbBigInt(limbs=(), negative=False)
        return LimbBigInt(limbs=tuple(prod), negative=(a.negative != b.negative))
