from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class HmmResult:
    states: Tuple[int, ...]
    log_prob: float

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "viterbi_hmm_decode_d60"
    version: int = 1
