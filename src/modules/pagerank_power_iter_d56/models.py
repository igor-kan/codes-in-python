from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class PageRankConfig:
    damping: float = 0.85
    iters: int = 40

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "pagerank_power_iter_d56"
    version: int = 1
