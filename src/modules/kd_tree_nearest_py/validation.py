import math
from typing import Sequence
from exceptions import KdTreeDimensionError, KdTreeDomainError


def validate_points(points: Sequence[Sequence[float]]) -> int:
    if not points or not points[0]:
        raise KdTreeDimensionError("points cannot be empty")
    dim = len(points[0])
    for p in points:
        if len(p) != dim:
            raise KdTreeDimensionError("inconsistent point dimensionality")
        if not all(math.isfinite(x) for x in p):
            raise KdTreeDomainError("non-finite coordinate")
    return dim
