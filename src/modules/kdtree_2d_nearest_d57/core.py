from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def build_kdtree(pts: List[Tuple[float, float]], depth: int = 0) -> Optional[KdNode]:
    if not pts:
        return None
    ax = depth % 2
    s = sorted(pts, key=lambda p: p[ax])
    mid = len(s) // 2
    return KdNode(
        pt=s[mid],
        axis=ax,
        left=build_kdtree(s[:mid], depth + 1),
        right=build_kdtree(s[mid + 1:], depth + 1),
    )

def kdtree_nearest_sq(root: Optional[KdNode], q: Tuple[float, float]) -> float:
    best = [float("inf")]

    def walk(node: Optional[KdNode]) -> None:
        if node is None:
            return
        dx = q[0] - node.pt[0]
        dy = q[1] - node.pt[1]
        d2 = dx * dx + dy * dy
        if d2 < best[0]:
            best[0] = d2
        diff = q[node.axis] - node.pt[node.axis]
        first, second = (node.left, node.right) if diff <= 0 else (node.right, node.left)
        walk(first)
        if diff * diff < best[0]:
            walk(second)

    walk(root)
    return best[0]
