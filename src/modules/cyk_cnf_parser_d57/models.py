from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

@dataclass(frozen=True)
class CnfRules:
    start: str

@dataclass(frozen=True)
class ModuleMeta:
    slug: str = "cyk_cnf_parser_d57"
    version: int = 1
