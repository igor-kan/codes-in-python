from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class Line:
    m: int
    b: int
    def eval(self, x: int) -> int: return self.m * x + self.b

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "li_chao_convex_line_py"
    version: int = 1
