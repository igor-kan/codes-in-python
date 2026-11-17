from typing import List, Protocol
from models import HeavyHitterResult

class HeavyExtractor(Protocol):
    def find_above_fraction(self, stream: List[int], k: int) -> HeavyHitterResult: ...
