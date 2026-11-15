"""Domain exception hierarchy for Hmm."""


class HmmError(ValueError):
    """Base domain error raised on precondition or numerical violations."""


class HmmDimensionError(HmmError):
    """Raised when inputs have incompatible or non-positive shapes."""


class HmmDomainError(HmmError):
    """Raised when arguments fall outside valid mathematical bounds."""
