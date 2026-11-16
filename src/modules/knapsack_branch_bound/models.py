from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class KnapsackItem:
    item_id: int
    weight: int
    value: int


@dataclass(frozen=True)
class KnapsackPlan:
    optimal_value: int
    total_weight: int
    selected_ids: Tuple[int, ...]
    explored_nodes: int
