from typing import Sequence

def fast_fold_ints(xs: Sequence[int]) -> int:
    acc = 1469598103934665603
    for x in xs:
        acc = ((acc ^ int(x)) * 1099511628211) & 0xFFFFFFFFFFFFFFFF
    return acc
