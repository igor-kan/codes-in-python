class ModuleError(Exception):
    """Base error for algorithmic module."""


class ValidationError(ModuleError):
    """Raised on invalid input dimensions or parameters."""


class InvariantError(ModuleError):
    """Raised when a runtime postcondition fails."""
