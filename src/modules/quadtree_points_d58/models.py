from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class AabbBox:
    x0: float
    y0: float
    x1: float
    y1: float

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "quadtree_points_d58"
    version: int = 1
