from typing import Protocol, Sequence
from models import XorFilterTable


class StaticSetFilter(Protocol):
    def build(self, keys: Sequence[int]) -> XorFilterTable:
        ...

    def contains(self, filt: XorFilterTable, key: int) -> bool:
        ...
