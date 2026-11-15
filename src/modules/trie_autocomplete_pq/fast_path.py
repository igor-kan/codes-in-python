from typing import List
from models import TrieNode


def count_prefix_matches(root: TrieNode, prefix: str) -> int:
    cur = root
    for ch in prefix:
        cur = cur.children.get(ch)
        if cur is None:
            return 0
    stack: List[TrieNode] = [cur]
    count = 0
    while stack:
        node = stack.pop()
        if node.is_terminal:
            count += 1
        stack.extend(node.children.values())
    return count
