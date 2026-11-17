from typing import List

def distinct_count(ids: List[int]) -> int:
    return len(set(ids))

def has_exact_k_distinct(ids: List[int], k: int) -> bool:
    return len(ids) == k and len(set(ids)) == k
