from fast_path import compile_and_eval
from exceptions import ExprEvalInvariantError

def verify_against_expected(expr: str, expected: int) -> None:
    got = compile_and_eval(expr)
    if got != expected:
        raise ExprEvalInvariantError(f'{expr} evaluated to {got} != {expected}')
