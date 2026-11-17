from typing import List
from core import EarleyParser

def fast_tokenize_expr(s: str) -> List[str]:
    return [ch for ch in s if not ch.isspace()]
