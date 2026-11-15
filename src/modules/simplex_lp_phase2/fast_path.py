from typing import Tuple
from models import LinearProgram


def compute_objective(c: Tuple[float, ...], x: Tuple[float, ...]) -> float:
    return sum(ci * xi for ci, xi in zip(c, x))
