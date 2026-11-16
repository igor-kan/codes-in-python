from typing import Sequence
from core import Xor16Filter
from models import XorFilterTable


def batch_probe_count(filt: XorFilterTable, queries: Sequence[int]) -> int:
    eng = Xor16Filter()
    return sum(1 for q in queries if eng.contains(filt, q))
