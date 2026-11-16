from typing import List, Sequence
from exceptions import XorFilterDomainError


def validate_xor_keys(keys: Sequence[int]) -> List[int]:
    if not isinstance(keys, (list, tuple, set)):
        raise XorFilterDomainError("keys must be concrete collection")
    return sorted(set(int(k) for k in keys))
