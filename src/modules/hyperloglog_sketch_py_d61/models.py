from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class HllEstimate:
    estimate: float
    registers: int

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "hyperloglog_sketch_py_d61"
    version: int = 1
