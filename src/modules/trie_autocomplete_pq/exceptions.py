"""Domain exception hierarchy for Trie."""


class TrieError(ValueError):
    """Base domain error raised on precondition or numerical violations."""


class TrieDimensionError(TrieError):
    """Raised when inputs have incompatible or non-positive shapes."""


class TrieDomainError(TrieError):
    """Raised when arguments fall outside valid mathematical bounds."""
