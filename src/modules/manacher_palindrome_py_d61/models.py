from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class PalindromeSpan:
    start: int
    length: int

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "manacher_palindrome_py_d61"
    version: int = 1
