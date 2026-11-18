from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class AcSummary:
    hits: int
    states: int

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "aho_corasick_multi_py"
    version: int = 1
