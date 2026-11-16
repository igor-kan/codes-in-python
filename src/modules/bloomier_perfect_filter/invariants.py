from typing import Sequence
from core import Xor16Filter
from exceptions import XorFilterDomainError
from models import XorFilterTable


def verify_zero_false_negatives(filt: XorFilterTable, keys: Sequence[int]) -> None:
    eng = Xor16Filter()
    for k in keys:
        if not eng.contains(filt, k):
            raise XorFilterDomainError(f"false negative for key={k}")
