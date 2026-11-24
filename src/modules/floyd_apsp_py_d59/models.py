from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class ApspSummary:
    neg_cycle: bool

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "floyd_apsp_py_d59"
    version: int = 1
