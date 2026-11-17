class IntervalDpError(Exception):
    """Base error for intervaldp module."""


class IntervalDpValidationError(IntervalDpError):
    """Raised on invalid shape, dimension, or boundary inputs."""


class IntervalDpInvariantError(IntervalDpError):
    """Raised when a runtime postcondition check fails."""
