from typing import List, Tuple

def is_valid_topo(n: int, edges: List[Tuple[int, int]], order: List[int]) -> bool:
    pos = [0] * n
    for idx, node in enumerate(order):
        pos[node] = idx
    return all(pos[u] < pos[v] for u, v in edges)
