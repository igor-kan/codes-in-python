"""Domain exception hierarchy for Router."""


class RouterError(ValueError):
    """Base domain error raised on precondition or numerical violations."""


class RouterDimensionError(RouterError):
    """Raised when inputs have incompatible or non-positive shapes."""


class RouterDomainError(RouterError):
    """Raised when arguments fall outside valid mathematical bounds."""
