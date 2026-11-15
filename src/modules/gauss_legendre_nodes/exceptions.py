"""Domain exception hierarchy for Quad."""


class QuadError(ValueError):
    """Base domain error raised on precondition or numerical violations."""


class QuadDimensionError(QuadError):
    """Raised when inputs have incompatible or non-positive shapes."""


class QuadDomainError(QuadError):
    """Raised when arguments fall outside valid mathematical bounds."""
