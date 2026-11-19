from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass
class PalNode:
    length: int
    link: int
    next: Dict[str, int]

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "eertree_palin_tree_py"
    version: int = 1
