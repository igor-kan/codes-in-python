from typing import List
from exceptions import CgValidationError

def check_spd_diag(a: List[List[float]]) -> None:
    for i, row in enumerate(a):
        if row[i] <= 0.0:
            raise CgValidationError('non-positive diagonal')
