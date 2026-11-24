from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class BloomConfig:
    bits: int = 256
    probes: int = 4

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "bloom_double_py_d59"
    version: int = 1
