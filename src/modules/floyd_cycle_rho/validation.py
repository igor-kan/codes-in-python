from exceptions import CycleDimensionError


def validate_budget(max_steps: int) -> None:
    if max_steps <= 0:
        raise CycleDimensionError("max_steps must be positive")
