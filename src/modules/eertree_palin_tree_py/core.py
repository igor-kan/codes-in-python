from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

class Eertree:
    def __init__(self, s: str) -> None:
        self.s = s
        self.nodes: List[PalNode] = [PalNode(-1, 0, {}), PalNode(0, 0, {})]
        self.suff = 1
        for i in range(len(s)):
            self._add(i)

    def _add(self, pos: int) -> None:
        cur = self.suff
        ch = self.s[pos]
        while True:
            l = self.nodes[cur].length
            if pos - 1 - l >= 0 and self.s[pos - 1 - l] == ch:
                break
            cur = self.nodes[cur].link
        if ch in self.nodes[cur].next:
            self.suff = self.nodes[cur].next[ch]
            return
        nw = len(self.nodes)
        nw_len = self.nodes[cur].length + 2
        self.nodes.append(PalNode(nw_len, 1, {}))
        self.nodes[cur].next[ch] = nw
        self.suff = nw
        if nw_len == 1:
            return
        while True:
            cur = self.nodes[cur].link
            l = self.nodes[cur].length
            if pos - 1 - l >= 0 and self.s[pos - 1 - l] == ch:
                self.nodes[nw].link = self.nodes[cur].next[ch]
                return

    def distinct_count(self) -> int:
        return len(self.nodes) - 2
