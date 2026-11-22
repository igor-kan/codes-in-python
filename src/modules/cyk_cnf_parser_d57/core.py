from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def cyk_accepts(term_rules: Dict[str, List[str]], bin_rules: List[Tuple[str, str, str]], start: str, tokens: List[str]) -> bool:
    n = len(tokens)
    if n == 0:
        return False
    table: List[List[set]] = [[set() for _ in range(n + 1)] for _ in range(n)]
    for i, tok in enumerate(tokens):
        for nt in term_rules.get(tok, []):
            table[i][1].add(nt)
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            for split in range(1, length):
                left = table[i][split]
                right = table[i + split][length - split]
                if not left or not right:
                    continue
                for lhs, b, c in bin_rules:
                    if b in left and c in right:
                        table[i][length].add(lhs)
    return start in table[0][n]
