from exceptions import TrieDimensionError, TrieDomainError


def validate_query(prefix: str, k: int) -> None:
    if k < 0:
        raise TrieDimensionError("k must be non-negative")
    if len(prefix) > 1024:
        raise TrieDomainError("prefix too long")
