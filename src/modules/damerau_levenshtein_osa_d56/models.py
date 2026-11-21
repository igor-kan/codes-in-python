from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class EditDistanceResult:
    distance: int
    similarity: float

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "damerau_levenshtein_osa_d56"
    version: int = 1
