from exceptions import ExprEvalValidationError

def check_balanced(expr: str) -> None:
    bal = 0
    for ch in expr:
        if ch == '(':
            bal += 1
        elif ch == ')':
            bal -= 1
            if bal < 0:
                raise ExprEvalValidationError('unbalanced parens')
    if bal != 0:
        raise ExprEvalValidationError('unclosed parens')
