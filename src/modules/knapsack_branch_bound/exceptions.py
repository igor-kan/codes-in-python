"""Domain exception hierarchy for Knapsack."""


class KnapsackError(ValueError):
    """Base domain error raised on precondition or numerical violations."""


class KnapsackDimensionError(KnapsackError):
    """Raised when inputs have incompatible or non-positive shapes."""


class KnapsackDomainError(KnapsackError):
    """Raised when arguments fall outside valid mathematical bounds."""
