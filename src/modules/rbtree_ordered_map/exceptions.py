"""Domain exception hierarchy for RbTree."""


class RbTreeError(ValueError):
    """Base domain error raised on precondition or numerical violations."""


class RbTreeDimensionError(RbTreeError):
    """Raised when inputs have incompatible or non-positive shapes."""


class RbTreeDomainError(RbTreeError):
    """Raised when arguments fall outside valid mathematical bounds."""
