from dataclasses import dataclass

@dataclass(frozen=True)
class WeightedItem:
    item_id: int
    weight: float
