class NelderMeadError(Exception):
    """Base error for neldermead module."""


class NelderMeadValidationError(NelderMeadError):
    """Raised on invalid shape, dimension, or boundary inputs."""


class NelderMeadInvariantError(NelderMeadError):
    """Raised when a runtime postcondition check fails."""
