from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class EditTrace:
    distance: int
    ops: List[str]

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "levenshtein_trace_d57"
    version: int = 1
