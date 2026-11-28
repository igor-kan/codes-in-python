from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class CuckooStats:
    capacity: int
    bucket_size: int
    count: int

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "cuckoo_filter_py_d61"
    version: int = 1
