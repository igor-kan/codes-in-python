"""Domain exception hierarchy for Fft."""


class FftError(ValueError):
    """Base domain error raised on precondition or numerical violations."""


class FftDimensionError(FftError):
    """Raised when inputs have incompatible or non-positive shapes."""


class FftDomainError(FftError):
    """Raised when arguments fall outside valid mathematical bounds."""
