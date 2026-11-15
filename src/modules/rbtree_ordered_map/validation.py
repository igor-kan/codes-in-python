from exceptions import RbTreeDomainError


def validate_range_bounds(lo: int, hi: int) -> None:
    if lo > hi:
        raise RbTreeDomainError(f"range lower bound {lo} exceeds upper bound {hi}")
