from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class XorFilterTable:
    block_len: int
    seed: int
    b: Tuple[int, ...]
    num_keys: int
