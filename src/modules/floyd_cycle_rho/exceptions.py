"""Domain exception hierarchy for Cycle."""


class CycleError(ValueError):
    """Base domain error raised on precondition or numerical violations."""


class CycleDimensionError(CycleError):
    """Raised when inputs have incompatible or non-positive shapes."""


class CycleDomainError(CycleError):
    """Raised when arguments fall outside valid mathematical bounds."""
