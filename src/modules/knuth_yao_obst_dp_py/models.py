from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class ObstSolution:
    cost: int
    root: int

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "knuth_yao_obst_dp_py"
    version: int = 1
