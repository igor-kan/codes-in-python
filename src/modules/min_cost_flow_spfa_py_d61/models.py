from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass
class McfEdge:
    to: int
    rev: int
    cap: int
    cost: int

@dataclass(frozen=True)
class McfResult:
    flow: int
    cost: int

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "min_cost_flow_spfa_py_d61"
    version: int = 1
