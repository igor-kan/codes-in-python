from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class DagEdge:
    u: int
    v: int
    weight: int = 1

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "topological_kahn_py_d60"
    version: int = 1
