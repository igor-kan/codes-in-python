from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass(frozen=True)
class KdNode:
    point: Tuple[float, ...]
    point_id: int
    axis: int
    left: Optional["KdNode"]
    right: Optional["KdNode"]


@dataclass(frozen=True)
class NeighborHit:
    point_id: int
    dist_sq: float
