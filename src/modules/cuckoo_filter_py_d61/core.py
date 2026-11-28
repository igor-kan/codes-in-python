from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

import hashlib


class CuckooFilter:
    def __init__(self, capacity: int = 64, bucket_size: int = 4, max_kicks: int = 64) -> None:
        if capacity <= 0 or bucket_size <= 0 or max_kicks <= 0:
            raise ValidationError("capacity, bucket size, and kick budget must be positive")
        width = 1
        while width < capacity:
            width <<= 1
        self.width = width
        self.bucket_size = bucket_size
        self.max_kicks = max_kicks
        self.buckets: List[List[int]] = [[] for _ in range(width)]
        self.count = 0

    @staticmethod
    def _hash64(item) -> int:
        raw = repr(item).encode("utf-8")
        return int.from_bytes(hashlib.blake2b(raw, digest_size=8).digest(), "big")

    @classmethod
    def _fingerprint(cls, item) -> int:
        return (cls._hash64(item) & 0xFFFF) or 1

    def _index(self, item) -> int:
        return self._hash64(item) & (self.width - 1)

    def _alternate(self, index: int, fingerprint: int) -> int:
        return (index ^ (fingerprint * 0x9E3779B1)) & (self.width - 1)

    def insert(self, item) -> bool:
        fp = self._fingerprint(item)
        i1 = self._index(item)
        i2 = self._alternate(i1, fp)
        for index in (i1, i2):
            if len(self.buckets[index]) < self.bucket_size:
                self.buckets[index].append(fp)
                self.count += 1
                return True
        index = i1
        current = fp
        state = (fp * 0x85EBCA6B + 1) & 0xFFFFFFFF
        for _ in range(self.max_kicks):
            state = (state * 1664525 + 1013904223) & 0xFFFFFFFF
            slot = state % len(self.buckets[index])
            self.buckets[index][slot], current = current, self.buckets[index][slot]
            index = self._alternate(index, current)
            if len(self.buckets[index]) < self.bucket_size:
                self.buckets[index].append(current)
                self.count += 1
                return True
        return False

    def contains(self, item) -> bool:
        fp = self._fingerprint(item)
        i1 = self._index(item)
        return fp in self.buckets[i1] or fp in self.buckets[self._alternate(i1, fp)]

    def remove(self, item) -> bool:
        fp = self._fingerprint(item)
        i1 = self._index(item)
        for index in (i1, self._alternate(i1, fp)):
            if fp in self.buckets[index]:
                self.buckets[index].remove(fp)
                self.count -= 1
                return True
        return False

    def stats(self) -> CuckooStats:
        return CuckooStats(capacity=self.width, bucket_size=self.bucket_size, count=self.count)
