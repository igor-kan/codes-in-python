class ExprEvalError(Exception):
    """Base error for expreval module."""


class ExprEvalValidationError(ExprEvalError):
    """Raised on invalid shape, dimension, or boundary inputs."""


class ExprEvalInvariantError(ExprEvalError):
    """Raised when a runtime postcondition check fails."""
