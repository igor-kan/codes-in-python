from typing import List, Protocol, Tuple
from models import DagSummary

class DagAnalyzer(Protocol):
    def analyze(self, n: int, edges: List[Tuple[int, int]], src: int) -> DagSummary: ...
