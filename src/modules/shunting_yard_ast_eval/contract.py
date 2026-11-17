from typing import List, Protocol

class ExpressionEngine(Protocol):
    def evaluate(self, expr: str) -> int: ...
