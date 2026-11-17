from dataclasses import dataclass
from typing import Dict, List

@dataclass(frozen=True)
class HeavyHitterResult:
    candidates: Dict[int, int]
    verified_counts: Dict[int, int]
