from exceptions import SimplexDimensionError, SimplexDomainError
from models import LinearProgram


def validate_lp(lp: LinearProgram) -> None:
    m = len(lp.a_rows)
    n = len(lp.c)
    if m <= 0 or n <= 0 or len(lp.b) != m:
        raise SimplexDimensionError("inconsistent LP dimensions")
    for row in lp.a_rows:
        if len(row) != n:
            raise SimplexDimensionError("constraint row width disagrees with objective c")
    for rhs in lp.b:
        if rhs < 0.0:
            raise SimplexDomainError("negative RHS requires phase-1 initialization")
