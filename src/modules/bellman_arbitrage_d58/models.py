from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class ArbitrageCheck:
    profitable: bool

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "bellman_arbitrage_d58"
    version: int = 1
