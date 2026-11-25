from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class AlignStep:
    op: str
    a_ch: str
    b_ch: str

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "edit_distance_hirschberg_d60"
    version: int = 1
