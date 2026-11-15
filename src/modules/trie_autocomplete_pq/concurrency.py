from concurrent.futures import ThreadPoolExecutor
from typing import List, Sequence
from core import WeightedPrefixTrie
from models import Suggestion


def parallel_autocomplete(trie: WeightedPrefixTrie, prefixes: Sequence[str], k: int = 5) -> List[List[Suggestion]]:
    with ThreadPoolExecutor(max_workers=2) as pool:
        return list(pool.map(lambda p: trie.top_k(p, k), prefixes))
