from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

class DeterministicTreap:
    def __init__(self) -> None:
        self._rng = 0x9E3779B97F4A7C15
        self.root: Optional[TreapNode] = None

    def _next_prio(self) -> int:
        self._rng = (self._rng * 6364136223846793005 + 1442695040888963407) & ((1 << 64) - 1)
        return self._rng

    @staticmethod
    def _sz(n: Optional[TreapNode]) -> int:
        return n.sz if n is not None else 0

    def _pull(self, n: TreapNode) -> TreapNode:
        n.sz = 1 + self._sz(n.left) + self._sz(n.right)
        return n

    def split(self, n: Optional[TreapNode], key: int) -> Tuple[Optional[TreapNode], Optional[TreapNode]]:
        if n is None:
            return None, None
        if n.key <= key:
            l, r = self.split(n.right, key)
            n.right = l
            return self._pull(n), r
        l, r = self.split(n.left, key)
        n.left = r
        return l, self._pull(n)

    def merge(self, a: Optional[TreapNode], b: Optional[TreapNode]) -> Optional[TreapNode]:
        if a is None:
            return b
        if b is None:
            return a
        if a.prio > b.prio:
            a.right = self.merge(a.right, b)
            return self._pull(a)
        b.left = self.merge(a, b.left)
        return self._pull(b)

    def insert(self, key: int) -> None:
        l, r = self.split(self.root, key)
        node = TreapNode(key=key, prio=self._next_prio())
        self.root = self.merge(self.merge(l, node), r)

    def kth(self, k: int) -> int:
        cur = self.root
        while cur is not None:
            lsz = self._sz(cur.left)
            if k == lsz:
                return cur.key
            if k < lsz:
                cur = cur.left
            else:
                k -= lsz + 1
                cur = cur.right
        raise ValidationError("k out of range")
