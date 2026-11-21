from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class EarleyItem:
    lhs: str
    rhs: Tuple[str, ...]
    dot: int
    start: int

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "earley_cfg_recogniser_d56"
    version: int = 1
