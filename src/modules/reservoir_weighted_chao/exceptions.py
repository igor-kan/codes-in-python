class WeightedSampleError(Exception):
    """Base error for weightedsample module."""


class WeightedSampleValidationError(WeightedSampleError):
    """Raised on invalid shape, dimension, or boundary inputs."""


class WeightedSampleInvariantError(WeightedSampleError):
    """Raised when a runtime postcondition check fails."""
