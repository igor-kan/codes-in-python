from typing import List, Protocol, Sequence, Tuple
from models import NeighborHit


class SpatialIndex(Protocol):
    def k_nearest(self, query: Sequence[float], k: int) -> List[NeighborHit]:
        ...

    def range_box(self, lo: Sequence[float], hi: Sequence[float]) -> List[int]:
        ...
