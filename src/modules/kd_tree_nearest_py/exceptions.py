"""Domain exception hierarchy for KdTree."""


class KdTreeError(ValueError):
    """Base domain error raised on precondition or numerical violations."""


class KdTreeDimensionError(KdTreeError):
    """Raised when inputs have incompatible or non-positive shapes."""


class KdTreeDomainError(KdTreeError):
    """Raised when arguments fall outside valid mathematical bounds."""
