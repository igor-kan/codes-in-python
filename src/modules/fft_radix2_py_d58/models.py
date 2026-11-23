from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class FftSpec:
    length: int

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "fft_radix2_py_d58"
    version: int = 1
