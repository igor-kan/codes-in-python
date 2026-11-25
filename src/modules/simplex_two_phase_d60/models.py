from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class LpSolution:
    objective: float
    primal: Tuple[float, ...]

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "simplex_two_phase_d60"
    version: int = 1
