from typing import List, Protocol, Sequence
from models import SpectrumResult


class SpectralEngine(Protocol):
    def forward(self, signal: Sequence[complex]) -> SpectrumResult:
        ...

    def inverse(self, spectrum: Sequence[complex]) -> List[complex]:
        ...
