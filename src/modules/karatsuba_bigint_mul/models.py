from dataclasses import dataclass
from typing import Tuple

LIMB_BASE = 10_000


@dataclass(frozen=True)
class LimbBigInt:
    limbs: Tuple[int, ...]
    negative: bool = False
