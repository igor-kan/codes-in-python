from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class CgReport:
    x: Tuple[float, ...]
    iterations: int
    residual: float

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "conjugate_grad_py_d60"
    version: int = 1
