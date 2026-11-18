from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class BipMatch:
    size: int
    pair_u: List[int]

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "hopcroft_karp_bipartite_py"
    version: int = 1
