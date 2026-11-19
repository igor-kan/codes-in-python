from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class AssignSolution:
    cost: int
    col_for_row: List[int]

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "hungarian_assign_o_n3_py"
    version: int = 1
