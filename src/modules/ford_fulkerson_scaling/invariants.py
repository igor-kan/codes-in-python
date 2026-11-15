from typing import Sequence
from models import DirectedCapEdge, MaxFlowReport


def verify_maxflow_mincut(n: int, edges: Sequence[DirectedCapEdge], source: int, sink: int, rep: MaxFlowReport) -> None:
    s_set = set(rep.min_cut_source_side)
    assert source in s_set and sink not in s_set
    cut_cap = sum(e.cap for e in edges if e.u in s_set and e.v not in s_set)
    assert cut_cap == rep.max_flow
