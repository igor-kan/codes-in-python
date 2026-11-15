from typing import Sequence
from exceptions import FlowDimensionError, FlowDomainError
from models import DirectedCapEdge


def validate_flow_network(n: int, edges: Sequence[DirectedCapEdge], source: int, sink: int) -> None:
    if n <= 1:
        raise FlowDimensionError("network must have at least 2 nodes")
    if not (0 <= source < n and 0 <= sink < n) or source == sink:
        raise FlowDomainError("invalid distinct source/sink indices")
    for e in edges:
        if not (0 <= e.u < n and 0 <= e.v < n) or e.cap < 0:
            raise FlowDomainError("edge endpoints out of bounds or negative capacity")
