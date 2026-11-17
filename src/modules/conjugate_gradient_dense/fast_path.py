from typing import List
from core import matvec

def residual_l2(a: List[List[float]], x: List[float], b: List[float]) -> float:
    import math
    ax = matvec(a, x)
    return math.sqrt(sum((u - v) ** 2 for u, v in zip(ax, b)))
