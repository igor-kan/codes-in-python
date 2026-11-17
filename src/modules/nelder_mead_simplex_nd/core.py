from typing import Callable, List
from models import SimplexResult
from exceptions import NelderMeadValidationError


def nelder_mead(fn: Callable[[List[float]], float], x0: List[float], max_iter: int = 500, tol: float = 1e-8) -> SimplexResult:
    n = len(x0)
    if n == 0 or max_iter <= 0:
        raise NelderMeadValidationError("x0 must be non-empty")
    simplex = [list(x0)]
    for i in range(n):
        v = list(x0)
        v[i] = v[i] + (0.05 if abs(v[i]) < 1e-6 else 0.05 * v[i])
        simplex.append(v)
    vals = [fn(v) for v in simplex]
    for it in range(1, max_iter + 1):
        order = sorted(range(n + 1), key=lambda k: vals[k])
        simplex = [simplex[k] for k in order]
        vals = [vals[k] for k in order]
        if max(abs(vals[k] - vals[0]) for k in range(1, n + 1)) <= tol:
            return SimplexResult(x=simplex[0], fval=vals[0], iters=it)
        cent = [sum(simplex[k][d] for k in range(n)) / n for d in range(n)]
        xr = [cent[d] + 1.0 * (cent[d] - simplex[-1][d]) for d in range(n)]
        fr = fn(xr)
        if vals[0] <= fr < vals[-2]:
            simplex[-1], vals[-1] = xr, fr
            continue
        if fr < vals[0]:
            xe = [cent[d] + 2.0 * (xr[d] - cent[d]) for d in range(n)]
            fe = fn(xe)
            simplex[-1], vals[-1] = (xe, fe) if fe < fr else (xr, fr)
            continue
        xc = [cent[d] + 0.5 * ((xr[d] if fr < vals[-1] else simplex[-1][d]) - cent[d]) for d in range(n)]
        fc = fn(xc)
        if fc < min(fr, vals[-1]):
            simplex[-1], vals[-1] = xc, fc
            continue
        for k in range(1, n + 1):
            simplex[k] = [simplex[0][d] + 0.5 * (simplex[k][d] - simplex[0][d]) for d in range(n)]
            vals[k] = fn(simplex[k])
    return SimplexResult(x=simplex[0], fval=vals[0], iters=max_iter)
