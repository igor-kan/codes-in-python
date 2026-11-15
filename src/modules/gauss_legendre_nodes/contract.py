from typing import Callable, Protocol
from models import GaussRule


class QuadratureRuleProtocol(Protocol):
    def generate_rule(self, order: int) -> GaussRule:
        ...

    def integrate(self, rule: GaussRule, fn: Callable[[float], float], a: float, b: float) -> float:
        ...
