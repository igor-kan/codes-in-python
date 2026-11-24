from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

class LfuCachePy:
    def __init__(self, cap: int) -> None:
        self.cap = cap
        self.vals: Dict[int, int] = {}
        self.freqs: Dict[int, int] = {}
        self.tiers: Dict[int, Dict[int, None]] = {}
        self.min_f = 0

    def _touch(self, key: int) -> None:
        f = self.freqs[key]
        del self.tiers[f][key]
        if not self.tiers[f] and self.min_f == f:
            self.min_f += 1
        self.freqs[key] = f + 1
        self.tiers.setdefault(f + 1, {})[key] = None

    def get(self, key: int) -> int:
        if key not in self.vals:
            return -1
        self._touch(key)
        return self.vals[key]

    def put(self, key: int, val: int) -> None:
        if self.cap <= 0:
            return
        if key in self.vals:
            self.vals[key] = val
            self._touch(key)
            return
        if len(self.vals) >= self.cap:
            evict = next(iter(self.tiers[self.min_f]))
            del self.tiers[self.min_f][evict]
            del self.vals[evict]
            del self.freqs[evict]
        self.vals[key] = val
        self.freqs[key] = 1
        self.tiers.setdefault(1, {})[key] = None
        self.min_f = 1
