from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def _lev(a: str, b: str) -> int:
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[-1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]

class BkTree:
    def __init__(self) -> None:
        self.root: Optional[BkNode] = None

    def add(self, word: str) -> None:
        if self.root is None:
            self.root = BkNode(word=word, children={})
            return
        cur = self.root
        while True:
            d = _lev(cur.word, word)
            if d == 0:
                return
            nxt = cur.children.get(d)
            if nxt is None:
                cur.children[d] = BkNode(word=word, children={})
                return
            cur = nxt

    def search(self, target: str, max_dist: int) -> List[str]:
        if self.root is None:
            return []
        hits: List[str] = []
        stk = [self.root]
        while stk:
            node = stk.pop()
            d = _lev(node.word, target)
            if d <= max_dist:
                hits.append(node.word)
            for k, child in node.children.items():
                if d - max_dist <= k <= d + max_dist:
                    stk.append(child)
        return sorted(hits)
