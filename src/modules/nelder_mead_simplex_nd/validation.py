from typing import List
from exceptions import NelderMeadValidationError

def validate_start(x0: List[float]) -> None:
    if not x0:
        raise NelderMeadValidationError('empty start vector')
