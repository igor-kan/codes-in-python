from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class CycleSignature(Generic[T]):
    tail_length: int
    period_length: int
    cycle_entry: T
