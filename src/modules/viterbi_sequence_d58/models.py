from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class HmmResult:
    path: List[int]
    logp: float

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "viterbi_sequence_d58"
    version: int = 1
