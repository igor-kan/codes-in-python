from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class CutSummary:
    weight: int
    phases: int

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "stoer_wagner_mincut_py"
    version: int = 1
