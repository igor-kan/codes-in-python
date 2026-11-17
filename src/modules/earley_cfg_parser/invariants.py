from typing import List
from core import EarleyParser
from exceptions import EarleyInvariantError

def verify_grammar_language(p: EarleyParser, valid: List[List[str]], invalid: List[List[str]]) -> None:
    for tok in valid:
        if not p.recognizes(tok):
            raise EarleyInvariantError(f'rejected valid string: {tok}')
    for tok in invalid:
        if p.recognizes(tok):
            raise EarleyInvariantError(f'accepted invalid string: {tok}')
