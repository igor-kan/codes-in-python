from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class SamStats:
    distinct: int
    states: int

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "suffix_automaton_dawg_py"
    version: int = 1
