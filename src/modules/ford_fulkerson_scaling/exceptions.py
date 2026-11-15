"""Domain exception hierarchy for Flow."""


class FlowError(ValueError):
    """Base domain error raised on precondition or numerical violations."""


class FlowDimensionError(FlowError):
    """Raised when inputs have incompatible or non-positive shapes."""


class FlowDomainError(FlowError):
    """Raised when arguments fall outside valid mathematical bounds."""
