from typing import Iterable, List, Protocol
from models import WeightedItem

class WeightedSampler(Protocol):
    def sample(self, stream: Iterable[WeightedItem], k: int, seed: int) -> List[int]: ...
