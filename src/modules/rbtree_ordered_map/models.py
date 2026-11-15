from dataclasses import dataclass
from typing import Optional

RED = True
BLACK = False


@dataclass
class RbNode:
    key: int
    value: int
    color: bool = RED
    left: Optional["RbNode"] = None
    right: Optional["RbNode"] = None
    parent: Optional["RbNode"] = None
