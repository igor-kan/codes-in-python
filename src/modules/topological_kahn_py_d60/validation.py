from exceptions import ValidationError

def require_positive(n: int) -> None:
    if n <= 0:
        raise ValidationError("n must be positive")
