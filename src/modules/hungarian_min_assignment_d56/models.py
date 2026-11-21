from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class AssignmentMatch:
    total_cost: float
    columns: List[int]

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "hungarian_min_assignment_d56"
    version: int = 1
