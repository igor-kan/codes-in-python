from typing import Protocol
from models import LimbBigInt


class MultiplierProtocol(Protocol):
    def multiply(self, a: LimbBigInt, b: LimbBigInt) -> LimbBigInt:
        ...
