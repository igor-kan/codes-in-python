from typing import Callable, TypeVar
from models import CycleSignature

T = TypeVar("T")


def brent_detect(step_fn: Callable[[T], T], start: T) -> CycleSignature[T]:
    power = 1
    lam = 1
    tortoise = start
    hare = step_fn(start)
    while tortoise != hare:
        if power == lam:
            tortoise = hare
            power <<= 1
            lam = 0
        hare = step_fn(hare)
        lam += 1

    tortoise = start
    hare = start
    for _ in range(lam):
        hare = step_fn(hare)

    mu = 0
    while tortoise != hare:
        tortoise = step_fn(tortoise)
        hare = step_fn(hare)
        mu += 1
    return CycleSignature(tail_length=mu, period_length=lam, cycle_entry=tortoise)
