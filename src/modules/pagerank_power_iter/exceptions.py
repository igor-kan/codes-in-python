"""Domain exception hierarchy for PageRank."""


class PageRankError(ValueError):
    """Base domain error raised on precondition or numerical violations."""


class PageRankDimensionError(PageRankError):
    """Raised when inputs have incompatible or non-positive shapes."""


class PageRankDomainError(PageRankError):
    """Raised when arguments fall outside valid mathematical bounds."""
