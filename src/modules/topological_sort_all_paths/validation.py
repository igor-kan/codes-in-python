from typing import List, Tuple
from exceptions import DagSortValidationError

def validate_edges(n: int, edges: List[Tuple[int, int]]) -> None:
    if n <= 0:
        raise DagSortValidationError('n must be > 0')
    for u, v in edges:
        if u == v or not (0 <= u < n and 0 <= v < n):
            raise DagSortValidationError('invalid edge')
