from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class GridCoord:
    r: int
    c: int

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "astar_manhattan_grid_d57"
    version: int = 1
