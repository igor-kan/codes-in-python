from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass
class KdNode:
    pt: Tuple[float, float]
    axis: int
    left: Optional["KdNode"] = None
    right: Optional["KdNode"] = None

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "kdtree_2d_nearest_d57"
    version: int = 1
