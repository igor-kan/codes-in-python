from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class CacheStats:
    capacity: int

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "lfu_cache_py_d59"
    version: int = 1
