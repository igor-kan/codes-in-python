from dataclasses import dataclass
from typing import Union

@dataclass(frozen=True)
class LitNode:
    val: int

@dataclass(frozen=True)
class BinOpNode:
    op: str
    left: 'ExprNode'
    right: 'ExprNode'

ExprNode = Union[LitNode, BinOpNode]
