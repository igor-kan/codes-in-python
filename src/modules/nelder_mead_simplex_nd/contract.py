from typing import Callable, List, Protocol
from models import SimplexResult

class DirectOptimizer(Protocol):
    def minimize(self, fn: Callable[[List[float]], float], x0: List[float]) -> SimplexResult: ...
