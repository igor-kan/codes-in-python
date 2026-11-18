from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class CartTree:
    root: int
    left: List[int]
    right: List[int]

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "cartesian_tree_rmq_py"
    version: int = 1
