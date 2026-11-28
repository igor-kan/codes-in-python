from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class QueensResult:
    n: int
    count: int
    first: Tuple[int, ...]

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "nqueens_bitset_py_d61"
    version: int = 1
