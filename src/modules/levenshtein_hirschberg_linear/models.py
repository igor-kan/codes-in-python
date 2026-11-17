from dataclasses import dataclass
from typing import List, Tuple

@dataclass(frozen=True)
class Alignment:
    distance: int
    aligned_a: str
    aligned_b: str
