class HeavyHitterError(Exception):
    """Base error for heavyhitter module."""


class HeavyHitterValidationError(HeavyHitterError):
    """Raised on invalid shape, dimension, or boundary inputs."""


class HeavyHitterInvariantError(HeavyHitterError):
    """Raised when a runtime postcondition check fails."""
