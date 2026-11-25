from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def build_kd_tree(points: List[Tuple[float, ...]], depth: int = 0) -> Optional[KdNode]:
    if not points:
        return None
    k = len(points[0])
    ax = depth % k
    pts = sorted(points, key=lambda p: p[ax])
    mid = len(pts) // 2
    return KdNode(
        point=pts[mid],
        axis=ax,
        left=build_kd_tree(pts[:mid], depth + 1),
        right=build_kd_tree(pts[mid + 1 :], depth + 1),
    )


def _sq_dist(a: Tuple[float, ...], b: Tuple[float, ...]) -> float:
    return sum((x - y) * (x - y) for x, y in zip(a, b))


def kd_nearest(root: Optional[KdNode], target: Tuple[float, ...]) -> Tuple[Tuple[float, ...], float]:
    if root is None:
        raise ValidationError("cannot query empty KD-tree")
    best_pt, best_d2 = root.point, _sq_dist(root.point, target)

    def rec(nd: Optional[KdNode]) -> None:
        nonlocal best_pt, best_d2
        if nd is None:
            return
        d2 = _sq_dist(nd.point, target)
        if d2 < best_d2:
            best_d2, best_pt = d2, nd.point
        diff = target[nd.axis] - nd.point[nd.axis]
        near, far = (nd.left, nd.right) if diff <= 0 else (nd.right, nd.left)
        rec(near)
        if diff * diff < best_d2:
            rec(far)

    rec(root)
    return best_pt, math.sqrt(best_d2)
