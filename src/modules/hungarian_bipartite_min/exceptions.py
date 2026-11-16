"""Domain exception hierarchy for Assignment."""


class AssignmentError(ValueError):
    """Base domain error raised on precondition or numerical violations."""


class AssignmentDimensionError(AssignmentError):
    """Raised when inputs have incompatible or non-positive shapes."""


class AssignmentDomainError(AssignmentError):
    """Raised when arguments fall outside valid mathematical bounds."""
