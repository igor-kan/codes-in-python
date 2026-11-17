from core import tokenize, to_rpn, build_ast, eval_ast

def compile_and_eval(expr: str) -> int:
    return eval_ast(build_ast(to_rpn(tokenize(expr))))
