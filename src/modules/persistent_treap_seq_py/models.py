from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class PTNode:
    val: int
    prio: int
    sz: int
    total: int
    l: Optional['PTNode'] = None
    r: Optional['PTNode'] = None

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "persistent_treap_seq_py"
    version: int = 1
