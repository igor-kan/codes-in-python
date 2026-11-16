"""Domain exception hierarchy for XorFilter."""


class XorFilterError(ValueError):
    """Base domain error raised on precondition or numerical violations."""


class XorFilterDimensionError(XorFilterError):
    """Raised when inputs have incompatible or non-positive shapes."""


class XorFilterDomainError(XorFilterError):
    """Raised when arguments fall outside valid mathematical bounds."""
