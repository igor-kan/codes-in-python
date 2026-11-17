from typing import Protocol
from models import Alignment

class LinearAligner(Protocol):
    def align(self, a: str, b: str) -> Alignment: ...
