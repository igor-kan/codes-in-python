from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class DistanceMatrix:
    dist: List[List[int]]

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "johnsons_apsp_heapq_py"
    version: int = 1
