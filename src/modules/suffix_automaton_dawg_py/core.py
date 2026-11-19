from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

class SuffixAutomaton:
    def __init__(self, s: str) -> None:
        self.len: List[int] = [0]
        self.link: List[int] = [-1]
        self.next: List[Dict[str, int]] = [{}]
        self.last = 0
        for ch in s:
            self._extend(ch)

    def _extend(self, ch: str) -> None:
        cur = len(self.len)
        self.len.append(self.len[self.last] + 1)
        self.link.append(0)
        self.next.append({})
        p = self.last
        while p != -1 and ch not in self.next[p]:
            self.next[p][ch] = cur
            p = self.link[p]
        if p == -1:
            self.link[cur] = 0
        else:
            q = self.next[p][ch]
            if self.len[p] + 1 == self.len[q]:
                self.link[cur] = q
            else:
                clone = len(self.len)
                self.len.append(self.len[p] + 1)
                self.link.append(self.link[q])
                self.next.append(dict(self.next[q]))
                while p != -1 and self.next[p].get(ch) == q:
                    self.next[p][ch] = clone
                    p = self.link[p]
                self.link[q] = self.link[cur] = clone
        self.last = cur

    def distinct_substrings(self) -> int:
        return sum(self.len[i] - self.len[self.link[i]] for i in range(1, len(self.len)))
