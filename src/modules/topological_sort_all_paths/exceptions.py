class DagSortError(Exception):
    """Base error for dagsort module."""


class DagSortValidationError(DagSortError):
    """Raised on invalid shape, dimension, or boundary inputs."""


class DagSortInvariantError(DagSortError):
    """Raised when a runtime postcondition check fails."""
