from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class JobInterval:
    start: int
    end: int
    weight: int
