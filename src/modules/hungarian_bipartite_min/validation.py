import math
from typing import Sequence, Tuple
from exceptions import AssignmentDimensionError, AssignmentDomainError


def validate_cost_matrix(cost_matrix: Sequence[Sequence[float]]) -> Tuple[int, int, bool]:
    if not cost_matrix or not cost_matrix[0]:
        raise AssignmentDimensionError("cost matrix must be non-empty")
    r = len(cost_matrix)
    c = len(cost_matrix[0])
    for row in cost_matrix:
        if len(row) != c:
            raise AssignmentDimensionError("cost matrix rows must share identical width")
        for x in row:
            if not math.isfinite(x):
                raise AssignmentDomainError("non-finite weight encountered")
    if r <= c:
        return r, c, False
    return c, r, True
