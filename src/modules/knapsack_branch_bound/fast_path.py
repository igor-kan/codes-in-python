from typing import Sequence
from models import KnapsackItem


def dp_oracle_value(items: Sequence[KnapsackItem], capacity: int) -> int:
    dp = [0] * (capacity + 1)
    for it in items:
        w, v = it.weight, it.value
        for cap in range(capacity, w - 1, -1):
            cand = dp[cap - w] + v
            if cand > dp[cap]:
                dp[cap] = cand
    return dp[capacity]
