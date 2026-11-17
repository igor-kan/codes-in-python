from typing import Dict, List, Set, Tuple
from models import EarleyItem
from exceptions import EarleyValidationError


class EarleyParser:
    def __init__(self, grammar: Dict[str, List[Tuple[str, ...]]], start_sym: str) -> None:
        if start_sym not in grammar:
            raise EarleyValidationError("missing start symbol")
        self.grammar = grammar
        self.start = start_sym
        self.nullable: Set[str] = set()
        changed = True
        while changed:
            changed = False
            for lhs, prods in grammar.items():
                if lhs not in self.nullable and any(all(sym in self.nullable for sym in rhs) for rhs in prods):
                    self.nullable.add(lhs)
                    changed = True

    def recognizes(self, tokens: List[str]) -> bool:
        n = len(tokens)
        charts: List[List[EarleyItem]] = [[] for _ in range(n + 1)]
        seen: List[Set[EarleyItem]] = [set() for _ in range(n + 1)]

        def add_item(k: int, it: EarleyItem) -> None:
            if it not in seen[k]:
                seen[k].add(it)
                charts[k].append(it)

        for rhs in self.grammar[self.start]:
            add_item(0, EarleyItem(self.start, rhs, 0, 0))

        for k in range(n + 1):
            i = 0
            while i < len(charts[k]):
                it = charts[k][i]
                i += 1
                if it.dot == len(it.rhs):
                    for prev in list(charts[it.origin]):
                        if prev.dot < len(prev.rhs) and prev.rhs[prev.dot] == it.lhs:
                            add_item(k, EarleyItem(prev.lhs, prev.rhs, prev.dot + 1, prev.origin))
                else:
                    nxt = it.rhs[it.dot]
                    if nxt in self.grammar:
                        for rhs in self.grammar[nxt]:
                            add_item(k, EarleyItem(nxt, rhs, 0, k))
                        if nxt in self.nullable:
                            add_item(k, EarleyItem(it.lhs, it.rhs, it.dot + 1, it.origin))
                    elif k < n and tokens[k] == nxt:
                        add_item(k + 1, EarleyItem(it.lhs, it.rhs, it.dot + 1, it.origin))
        return any(it.lhs == self.start and it.dot == len(it.rhs) and it.origin == 0 for it in charts[n])
