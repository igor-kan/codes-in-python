from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class SieveSummary:
    limit: int
    primes: int

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "segmented_sieve_py_d61"
    version: int = 1
