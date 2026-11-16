import heapq
from typing import List, Optional, Sequence, Tuple
from models import KdNode, NeighborHit
from validation import validate_points


def _dist_sq(a: Sequence[float], b: Sequence[float]) -> float:
    return sum((x - y) * (x - y) for x, y in zip(a, b))


class KdTreeIndex:
    def __init__(self, points: Sequence[Sequence[float]]) -> None:
        self.dim = validate_points(points)
        indexed = [(tuple(float(v) for v in p), idx) for idx, p in enumerate(points)]
        self.root = self._build(indexed, 0)

    def _build(self, pts: List[Tuple[Tuple[float, ...], int]], depth: int) -> Optional[KdNode]:
        if not pts:
            return None
        axis = depth % self.dim
        pts.sort(key=lambda item: item[0][axis])
        mid = len(pts) >> 1
        return KdNode(
            point=pts[mid][0],
            point_id=pts[mid][1],
            axis=axis,
            left=self._build(pts[:mid], depth + 1),
            right=self._build(pts[mid + 1:], depth + 1),
        )

    def k_nearest(self, query: Sequence[float], k: int) -> List[NeighborHit]:
        if k <= 0 or self.root is None:
            return []
        heap: List[Tuple[float, int]] = []  # max-heap using -dist_sq

        def search(node: Optional[KdNode]) -> None:
            if node is None:
                return
            d2 = _dist_sq(query, node.point)
            if len(heap) < k:
                heapq.heappush(heap, (-d2, node.point_id))
            elif d2 < -heap[0][0]:
                heapq.heapreplace(heap, (-d2, node.point_id))
            diff = query[node.axis] - node.point[node.axis]
            near, far = (node.left, node.right) if diff <= 0.0 else (node.right, node.left)
            search(near)
            if len(heap) < k or (diff * diff) <= -heap[0][0]:
                search(far)

        search(self.root)
        hits = [NeighborHit(pid, -neg_d2) for neg_d2, pid in heap]
        hits.sort(key=lambda h: (h.dist_sq, h.point_id))
        return hits

    def range_box(self, lo: Sequence[float], hi: Sequence[float]) -> List[int]:
        out: List[int] = []

        def dfs(node: Optional[KdNode]) -> None:
            if node is None:
                return
            if all(a <= x <= b for a, x, b in zip(lo, node.point, hi)):
                out.append(node.point_id)
            ax = node.axis
            if lo[ax] <= node.point[ax]:
                dfs(node.left)
            if hi[ax] >= node.point[ax]:
                dfs(node.right)

        dfs(self.root)
        out.sort()
        return out
