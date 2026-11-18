from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

class LiChaoTree:
    def __init__(self, dom: int) -> None:
        self.dom = dom
        self.tree = [Line(0, 10**18)] * (4 * dom + 4)

    def add_line(self, m: int, b: int) -> None:
        self._ins(1, 0, self.dom - 1, Line(m, b))

    def _ins(self, v: int, l: int, r: int, nw: Line) -> None:
        mid = (l + r) >> 1
        lb = nw.eval(l) < self.tree[v].eval(l)
        mb = nw.eval(mid) < self.tree[v].eval(mid)
        if mb:
            self.tree[v], nw = nw, self.tree[v]
        if l == r:
            return
        if lb != mb:
            self._ins(v << 1, l, mid, nw)
        else:
            self._ins(v << 1 | 1, mid + 1, r, nw)

    def query(self, x: int) -> int:
        v, l, r, best = 1, 0, self.dom - 1, 10**18
        while True:
            best = min(best, self.tree[v].eval(x))
            if l == r:
                return best
            mid = (l + r) >> 1
            if x <= mid:
                v, r = v << 1, mid
            else:
                v, l = v << 1 | 1, mid + 1
