from typing import List
from models import WeightedItem
from exceptions import WeightedSampleValidationError

def validate_positive_weights(items: List[WeightedItem]) -> None:
    if any(it.weight <= 0.0 for it in items):
        raise WeightedSampleValidationError('non-positive weight')
