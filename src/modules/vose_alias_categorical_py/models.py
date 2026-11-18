from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class AliasTable:
    prob: List[float]
    alias: List[int]

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "vose_alias_categorical_py"
    version: int = 1
