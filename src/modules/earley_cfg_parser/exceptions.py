class EarleyError(Exception):
    """Base error for earley module."""


class EarleyValidationError(EarleyError):
    """Raised on invalid shape, dimension, or boundary inputs."""


class EarleyInvariantError(EarleyError):
    """Raised when a runtime postcondition check fails."""
