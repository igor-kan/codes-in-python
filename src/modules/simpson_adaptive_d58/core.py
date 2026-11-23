from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def adaptive_simpson(fn, a: float, b: float, tol: float = 1e-9, max_depth: int = 12) -> float:
    def simpson_step(x0: float, x2: float) -> Tuple[float, float, float, float]:
        xm = 0.5 * (x0 + x2)
        f0, fm, f2 = fn(x0), fn(xm), fn(x2)
        return (x2 - x0) / 6.0 * (f0 + 4.0 * fm + f2), f0, fm, f2

    def recurse(x0: float, x2: float, whole: float, f0: float, fm: float, f2: float, eps: float, depth: int) -> float:
        xm = 0.5 * (x0 + x2)
        fl = fn(0.5 * (x0 + xm))
        fr = fn(0.5 * (xm + x2))
        left = (xm - x0) / 6.0 * (f0 + 4.0 * fl + fm)
        right = (x2 - xm) / 6.0 * (fm + 4.0 * fr + f2)
        delta = left + right - whole
        if depth <= 0 or abs(delta) <= 15.0 * eps:
            return left + right + delta / 15.0
        return (
            recurse(x0, xm, left, f0, fl, fm, eps * 0.5, depth - 1)
            + recurse(xm, x2, right, fm, fr, f2, eps * 0.5, depth - 1)
        )

    w, f0, fm, f2 = simpson_step(a, b)
    return recurse(a, b, w, f0, fm, f2, tol, max_depth)
