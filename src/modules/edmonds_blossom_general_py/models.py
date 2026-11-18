from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class GeneralMatching:
    pairs: int
    mate: List[int]

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "edmonds_blossom_general_py"
    version: int = 1
