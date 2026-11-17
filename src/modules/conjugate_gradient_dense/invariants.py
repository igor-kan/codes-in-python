from typing import List
from fast_path import residual_l2
from exceptions import CgInvariantError

def verify_residual(a: List[List[float]], x: List[float], b: List[float], tol: float = 1e-9) -> None:
    if residual_l2(a, x, b) > tol:
        raise CgInvariantError('residual above tolerance')
