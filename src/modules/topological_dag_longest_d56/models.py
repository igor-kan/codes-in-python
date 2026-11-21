from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class CriticalMetrics:
    makespan: int
    dist: List[int]

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "topological_dag_longest_d56"
    version: int = 1
