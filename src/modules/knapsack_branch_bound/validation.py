from typing import Sequence
from exceptions import KnapsackDimensionError, KnapsackDomainError
from models import KnapsackItem


def validate_knapsack_input(items: Sequence[KnapsackItem], capacity: int) -> None:
    if capacity < 0:
        raise KnapsackDomainError("capacity must be non-negative")
    seen = set()
    for it in items:
        if it.weight <= 0 or it.value < 0:
            raise KnapsackDimensionError("item weights must be > 0 and values >= 0")
        if it.item_id in seen:
            raise KnapsackDomainError(f"duplicate item_id {it.item_id}")
        seen.add(it.item_id)
