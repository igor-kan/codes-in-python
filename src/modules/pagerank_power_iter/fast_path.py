from typing import List, Tuple
from models import PageRankResult


def top_k_nodes(res: PageRankResult, k: int) -> List[Tuple[int, float]]:
    pairs = sorted(enumerate(res.ranks), key=lambda kv: (-kv[1], kv[0]))
    return pairs[:k]
