from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def karatsuba_mul(x: int, y: int) -> int:
    if x < 10000 or y < 10000:
        return x * y
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    p = 10 ** m
    x1, x0 = divmod(x, p)
    y1, y0 = divmod(y, p)
    z0 = karatsuba_mul(x0, y0)
    z2 = karatsuba_mul(x1, y1)
    z1 = karatsuba_mul(x0 + x1, y0 + y1) - z2 - z0
    return z2 * (10 ** (2 * m)) + z1 * p + z0
