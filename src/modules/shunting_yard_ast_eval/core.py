import re
from typing import List
from models import BinOpNode, ExprNode, LitNode
from exceptions import ExprEvalValidationError

_PREC = {"+": 1, "-": 1, "*": 2, "/": 2}


def tokenize(expr: str) -> List[str]:
    toks = re.findall(r"\d+|[+\-*/()]", expr)
    if not toks:
        raise ExprEvalValidationError("empty expression")
    return toks


def to_rpn(tokens: List[str]) -> List[str]:
    out: List[str] = []
    ops: List[str] = []
    for tok in tokens:
        if tok.isdigit():
            out.append(tok)
        elif tok in _PREC:
            while ops and ops[-1] in _PREC and _PREC[ops[-1]] >= _PREC[tok]:
                out.append(ops.pop())
            ops.append(tok)
        elif tok == "(":
            ops.append(tok)
        elif tok == ")":
            while ops and ops[-1] != "(":
                out.append(ops.pop())
            if not ops:
                raise ExprEvalValidationError("mismatched closing paren")
            ops.pop()
    while ops:
        op = ops.pop()
        if op == "(":
            raise ExprEvalValidationError("unclosed paren")
        out.append(op)
    return out


def build_ast(rpn: List[str]) -> ExprNode:
    st: List[ExprNode] = []
    for tok in rpn:
        if tok.isdigit():
            st.append(LitNode(int(tok)))
        else:
            if len(st) < 2:
                raise ExprEvalValidationError("insufficient operands")
            r = st.pop()
            l = st.pop()
            st.append(BinOpNode(tok, l, r))
    if len(st) != 1:
        raise ExprEvalValidationError("trailing expression tokens")
    return st[0]


def eval_ast(node: ExprNode) -> int:
    if isinstance(node, LitNode):
        return node.val
    lv = eval_ast(node.left)
    rv = eval_ast(node.right)
    if node.op == "+":
        return lv + rv
    if node.op == "-":
        return lv - rv
    if node.op == "*":
        return lv * rv
    if rv == 0:
        raise ExprEvalValidationError("division by zero")
    return lv // rv
