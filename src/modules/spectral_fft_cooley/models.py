from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class SpectrumResult:
    bins: Tuple[complex, ...]
    time_energy: float
    freq_energy: float
