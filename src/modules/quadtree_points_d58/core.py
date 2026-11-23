from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

class QuadNode:
    def __init__(self, x0: float, y0: float, x1: float, y1: float, cap: int = 4) -> None:
        self.box = (x0, y0, x1, y1)
        self.cap = cap
        self.pts: List[Tuple[float, float]] = []
        self.kids: Optional[List["QuadNode"]] = None

    def _subdivide(self) -> None:
        x0, y0, x1, y1 = self.box
        mx, my = 0.5 * (x0 + x1), 0.5 * (y0 + y1)
        self.kids = [
            QuadNode(x0, y0, mx, my, self.cap),
            QuadNode(mx, y0, x1, my, self.cap),
            QuadNode(x0, my, mx, y1, self.cap),
            QuadNode(mx, my, x1, y1, self.cap),
        ]

    def insert(self, pt: Tuple[float, float]) -> bool:
        x0, y0, x1, y1 = self.box
        px, py = pt
        if not (x0 <= px <= x1 and y0 <= py <= y1):
            return False
        if self.kids is None:
            if len(self.pts) < self.cap:
                self.pts.append(pt)
                return True
            self._subdivide()
        assert self.kids is not None
        return any(k.insert(pt) for k in self.kids)

    def query_box(self, qx0: float, qy0: float, qx1: float, qy1: float) -> List[Tuple[float, float]]:
        x0, y0, x1, y1 = self.box
        if x1 < qx0 or qx1 < x0 or y1 < qy0 or qy1 < y0:
            return []
        hits = [p for p in self.pts if qx0 <= p[0] <= qx1 and qy0 <= p[1] <= qy1]
        if self.kids is not None:
            for k in self.kids:
                hits.extend(k.query_box(qx0, qy0, qx1, qy1))
        return hits
