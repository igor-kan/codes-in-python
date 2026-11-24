from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class SuffixLcpMeta:
    length: int
    distinct_substrings: int

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "suffix_array_py_d59"
    version: int = 1
