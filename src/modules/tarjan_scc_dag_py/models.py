from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class SccResult:
    comp_ids: Tuple[int, ...]
    components: Tuple[Tuple[int, ...], ...]
    condensation_edges: Tuple[Tuple[int, int], ...]
