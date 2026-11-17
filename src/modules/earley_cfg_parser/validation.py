from typing import Dict, List, Tuple
from exceptions import EarleyValidationError

def validate_grammar(grammar: Dict[str, List[Tuple[str, ...]]], start: str) -> None:
    if not grammar or start not in grammar:
        raise EarleyValidationError('invalid CFG grammar')
