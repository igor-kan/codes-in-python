from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass
class TreapNode:
    key: int
    prio: int
    sz: int = 1
    left: Optional["TreapNode"] = None
    right: Optional["TreapNode"] = None

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "splay_treap_split_merge_d56"
    version: int = 1
