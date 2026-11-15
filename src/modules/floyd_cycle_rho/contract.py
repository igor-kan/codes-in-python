from typing import Callable, Protocol, TypeVar
from models import CycleSignature

T = TypeVar("T")


class CycleDetectorProtocol(Protocol[T]):
    def detect(self, step_fn: Callable[[T], T], start: T, max_steps: int) -> CycleSignature[T]:
        ...
