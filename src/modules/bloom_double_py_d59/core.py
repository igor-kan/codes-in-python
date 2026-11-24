from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

class IntBitBloom:
    def __init__(self, bits: int = 256, probes: int = 4) -> None:
        self.bits = bits
        self.probes = probes
        self.mask = 0

    def _pair(self, key: int) -> Tuple[int, int]:
        h1 = ((key ^ (key >> 30)) * 0xBF58476D1CE4E5B9) & 0xFFFFFFFFFFFFFFFF
        h2 = (((key * 0x94D049BB133111EB) >> 32) | 1) & 0xFFFFFFFFFFFFFFFF
        return h1, h2

    def add(self, key: int) -> None:
        h1, h2 = self._pair(key)
        for i in range(self.probes):
            self.mask |= 1 << ((h1 + i * h2) % self.bits)

    def might_contain(self, key: int) -> bool:
        h1, h2 = self._pair(key)
        for i in range(self.probes):
            if not (self.mask & (1 << ((h1 + i * h2) % self.bits))):
                return False
        return True
