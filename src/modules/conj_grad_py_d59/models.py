from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class CgStatus:
    iters: int
    residual: float

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "conj_grad_py_d59"
    version: int = 1
