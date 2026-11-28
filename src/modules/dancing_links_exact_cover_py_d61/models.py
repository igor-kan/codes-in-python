from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class ExactCoverResult:
    solutions: Tuple[Tuple[int, ...], ...]
    columns: int

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "dancing_links_exact_cover_py_d61"
    version: int = 1
