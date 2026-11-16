"""Domain exception hierarchy for TarjanScc."""


class TarjanSccError(ValueError):
    """Base domain error raised on precondition or numerical violations."""


class TarjanSccDimensionError(TarjanSccError):
    """Raised when inputs have incompatible or non-positive shapes."""


class TarjanSccDomainError(TarjanSccError):
    """Raised when arguments fall outside valid mathematical bounds."""
