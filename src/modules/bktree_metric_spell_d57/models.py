from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass
class BkNode:
    word: str
    children: Dict[int, "BkNode"]

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "bktree_metric_spell_d57"
    version: int = 1
