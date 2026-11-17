from typing import List, Tuple
from models import DagSummary
from fast_path import is_valid_topo
from exceptions import DagSortInvariantError

def verify_dag_summary(n: int, edges: List[Tuple[int, int]], res: DagSummary) -> None:
    if len(res.order) != n or not is_valid_topo(n, edges, res.order):
        raise DagSortInvariantError('invalid topological order')
