from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class CholMeta:
    order: int

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "cholesky_spd_py_d59"
    version: int = 1
