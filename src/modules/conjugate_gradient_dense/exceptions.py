class CgError(Exception):
    """Base error for cg module."""


class CgValidationError(CgError):
    """Raised on invalid shape, dimension, or boundary inputs."""


class CgInvariantError(CgError):
    """Raised when a runtime postcondition check fails."""
