from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def _matvec(a: List[List[float]], v: List[float]) -> List[float]:
    return [sum(row[j] * v[j] for j in range(len(v))) for row in a]


def _dot(u: List[float], v: List[float]) -> float:
    return sum(ui * vi for ui, vi in zip(u, v))


def conjugate_gradient(a: List[List[float]], b: List[float], tol: float = 1e-10) -> CgReport:
    n = len(b)
    if n == 0:
        raise ValidationError("empty linear system")
    x = [0.0] * n
    r = [float(bi) for bi in b]
    p = list(r)
    rs_old = _dot(r, r)
    iters = 0
    for k in range(max(n * 2, 10)):
        if math.sqrt(rs_old) < tol:
            break
        iters = k + 1
        ap = _matvec(a, p)
        denom = _dot(p, ap)
        if abs(denom) < 1e-18:
            break
        alpha = rs_old / denom
        x = [x[i] + alpha * p[i] for i in range(n)]
        r = [r[i] - alpha * ap[i] for i in range(n)]
        rs_new = _dot(r, r)
        if math.sqrt(rs_new) < tol:
            rs_old = rs_new
            break
        beta = rs_new / rs_old
        p = [r[i] + beta * p[i] for i in range(n)]
        rs_old = rs_new
    return CgReport(x=tuple(x), iterations=iters, residual=math.sqrt(rs_old))
