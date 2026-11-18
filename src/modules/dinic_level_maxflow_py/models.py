from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass
class FlowEdge:
    to: int
    rev: int
    cap: int

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "dinic_level_maxflow_py"
    version: int = 1
