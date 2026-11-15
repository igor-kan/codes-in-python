"""Domain exception hierarchy for BigInt."""


class BigIntError(ValueError):
    """Base domain error raised on precondition or numerical violations."""


class BigIntDimensionError(BigIntError):
    """Raised when inputs have incompatible or non-positive shapes."""


class BigIntDomainError(BigIntError):
    """Raised when arguments fall outside valid mathematical bounds."""
