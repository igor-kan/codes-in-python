from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class CodeTable:
    codes: Dict[str, str]

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "huffman_prefix_codec_d56"
    version: int = 1
