from dataclasses import dataclass
from typing import Dict, List, Tuple

@dataclass(frozen=True)
class EarleyItem:
    lhs: str
    rhs: Tuple[str, ...]
    dot: int
    origin: int
