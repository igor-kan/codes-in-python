from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def cg_solve(A: List[List[float]], b: List[float], tol: float = 1e-10) -> List[float]:
    n = len(b)
    x = [0.0] * n

    def matvec(v: List[float]) -> List[float]:
        return [sum(A[i][j] * v[j] for j in range(n)) for i in range(n)]

    def dot(u: List[float], v: List[float]) -> float:
        return sum(ui * vi for ui, vi in zip(u, v))

    r = list(b)
    p = list(r)
    rsold = dot(r, r)
    for _ in range(2 * n + 10):
        if math.sqrt(rsold) < tol:
            break
        ap = matvec(p)
        alpha = rsold / dot(p, ap)
        x = [xi + alpha * pi for xi, pi in zip(x, p)]
        r = [ri - alpha * api for ri, api in zip(r, ap)]
        rsnew = dot(r, r)
        beta = rsnew / rsold
        p = [ri + beta * pi for ri, pi in zip(r, p)]
        rsold = rsnew
    return x
