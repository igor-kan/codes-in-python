from typing import Callable, TypeVar
from models import CycleSignature

T = TypeVar("T")


def verify_cycle_signature(step_fn: Callable[[T], T], start: T, sig: CycleSignature[T]) -> None:
    assert sig.tail_length >= 0 and sig.period_length >= 1
    cur = start
    for _ in range(sig.tail_length):
        cur = step_fn(cur)
    assert cur == sig.cycle_entry
    after = cur
    for _ in range(sig.period_length):
        after = step_fn(after)
    assert after == cur
