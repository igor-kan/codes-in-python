from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass
class KdNode:
    point: Tuple[float, ...]
    axis: int
    left: Optional["KdNode"] = None
    right: Optional["KdNode"] = None

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "kd_tree_nearest_py_d60"
    version: int = 1
