"""Domain exception hierarchy for Simplex."""


class SimplexError(ValueError):
    """Base domain error raised on precondition or numerical violations."""


class SimplexDimensionError(SimplexError):
    """Raised when inputs have incompatible or non-positive shapes."""


class SimplexDomainError(SimplexError):
    """Raised when arguments fall outside valid mathematical bounds."""
