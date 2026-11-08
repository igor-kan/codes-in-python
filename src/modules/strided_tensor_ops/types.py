"""
Core type definitions and operational interfaces for NumPy C-Contiguous Strided Slicing and Contractions.
Module: strided_tensor_ops
"""

from dataclasses import dataclass, field
from typing import Optional, List, Any
from enum import Enum, auto

ALIGNMENT: int = 64

class ModuleErrorCode(Enum):
    SUCCESS = 0
    NULL_POINTER = auto()
    INVALID_PARAM = auto()
    OUT_OF_BOUNDS = auto()
    CONVERGENCE_FAILURE = auto()

@dataclass
class ModuleConfig:
    capacity: int = 1024
    tolerance: float = 1e-12
    max_iterations: int = 1000
    flags: int = 0

@dataclass
class ModuleContext:
    config: ModuleConfig = field(default_factory=ModuleConfig)
    operations_count: int = 0
    state: Optional[Any] = None
