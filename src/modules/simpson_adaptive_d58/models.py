from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class QuadEstimate:
    integral: float
    tol: float

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "simpson_adaptive_d58"
    version: int = 1
