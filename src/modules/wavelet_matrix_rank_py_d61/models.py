from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class WaveletSpan:
    lo: int
    hi: int

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "wavelet_matrix_rank_py_d61"
    version: int = 1
