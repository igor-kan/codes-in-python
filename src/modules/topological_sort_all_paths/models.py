from dataclasses import dataclass
from typing import Dict, List, Tuple

@dataclass(frozen=True)
class DagSummary:
    order: List[int]
    longest_dist: List[int]
    path_counts: List[int]
