from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class GaussRule:
    order: int
    nodes: Tuple[float, ...]
    weights: Tuple[float, ...]
