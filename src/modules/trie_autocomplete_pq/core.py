import heapq
from typing import List, Tuple
from exceptions import TrieDomainError
from models import Suggestion, TrieNode


class WeightedPrefixTrie:
    def __init__(self) -> None:
        self.root = TrieNode()
        self.term_count = 0

    def insert(self, term: str, weight: int = 1) -> None:
        if not term or weight <= 0:
            raise TrieDomainError("term must be non-empty with positive weight")
        cur = self.root
        for ch in term:
            nxt = cur.children.get(ch)
            if nxt is None:
                nxt = TrieNode()
                cur.children[ch] = nxt
            cur = nxt
        if not cur.is_terminal:
            self.term_count += 1
        cur.is_terminal = True
        cur.frequency += weight

    def top_k(self, prefix: str, k: int) -> List[Suggestion]:
        if k <= 0:
            return []
        cur = self.root
        for ch in prefix:
            cur = cur.children.get(ch)
            if cur is None:
                return []
        collected: List[Tuple[int, str]] = []

        def dfs(node: TrieNode, buf: List[str]) -> None:
            if node.is_terminal:
                collected.append((-node.frequency, "".join(buf)))
            for ch in sorted(node.children):
                buf.append(ch)
                dfs(node.children[ch], buf)
                buf.pop()

        dfs(cur, list(prefix))
        best = heapq.nsmallest(k, collected)
        return [Suggestion(term=w, score=-neg_f) for neg_f, w in best]
