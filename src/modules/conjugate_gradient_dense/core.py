import math
from typing import List
from models import CgSolution
from exceptions import CgValidationError


def dot(u: List[float], v: List[float]) -> float:
    return sum(x * y for x, y in zip(u, v))


def matvec(a: List[List[float]], v: List[float]) -> List[float]:
    return [dot(row, v) for row in a]


def solve_pcg(a: List[List[float]], b: List[float], tol: float = 1e-11, max_iter: int = 300) -> CgSolution:
    n = len(b)
    if n == 0 or len(a) != n or any(len(row) != n or row[i] <= 0.0 for i, row in enumerate(a)):
        raise CgValidationError("matrix must be square with positive diagonal")
    x = [0.0] * n
    minv = [1.0 / a[i][i] for i in range(n)]
    ax = matvec(a, x)
    r = [bi - axi for bi, axi in zip(b, ax)]
    z = [mi * ri for mi, ri in zip(minv, r)]
    p = list(z)
    rz_old = dot(r, z)
    for k in range(1, max_iter + 1):
        res = math.sqrt(dot(r, r))
        if res <= tol:
            return CgSolution(x=x, iters=k - 1, residual=res)
        ap = matvec(a, p)
        pap = dot(p, ap)
        if pap <= 1e-30:
            break
        alpha = rz_old / pap
        x = [xi + alpha * pi for xi, pi in zip(x, p)]
        r = [ri - alpha * api for ri, api in zip(r, ap)]
        z = [mi * ri for mi, ri in zip(minv, r)]
        rz_new = dot(r, z)
        beta = rz_new / rz_old
        p = [zi + beta * pi for zi, pi in zip(z, p)]
        rz_old = rz_new
    return CgSolution(x=x, iters=max_iter, residual=math.sqrt(dot(r, r)))
