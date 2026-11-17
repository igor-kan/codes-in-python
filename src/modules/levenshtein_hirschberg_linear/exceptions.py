class HirschbergError(Exception):
    """Base error for hirschberg module."""


class HirschbergValidationError(HirschbergError):
    """Raised on invalid shape, dimension, or boundary inputs."""


class HirschbergInvariantError(HirschbergError):
    """Raised when a runtime postcondition check fails."""
