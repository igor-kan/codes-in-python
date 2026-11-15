from typing import Callable, TypeVar
from exceptions import CycleDomainError
from models import CycleSignature

T = TypeVar("T")


class FloydCycleDetector:
    def detect(self, step_fn: Callable[[T], T], start: T, max_steps: int = 1_000_000) -> CycleSignature[T]:
        tortoise = step_fn(start)
        hare = step_fn(step_fn(start))
        steps = 1
        while tortoise != hare:
            if steps >= max_steps:
                raise CycleDomainError("step budget exceeded without detecting cycle")
            tortoise = step_fn(tortoise)
            hare = step_fn(step_fn(hare))
            steps += 1

        mu = 0
        tortoise = start
        while tortoise != hare:
            tortoise = step_fn(tortoise)
            hare = step_fn(hare)
            mu += 1

        lam = 1
        hare = step_fn(tortoise)
        while tortoise != hare:
            hare = step_fn(hare)
            lam += 1

        return CycleSignature(tail_length=mu, period_length=lam, cycle_entry=tortoise)
