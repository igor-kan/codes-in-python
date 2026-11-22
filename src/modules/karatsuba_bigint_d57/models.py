from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class BigIntStats:
    digits: int
    cutoff: int = 32

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "karatsuba_bigint_d57"
    version: int = 1
