from dataclasses import dataclass
from typing import Sequence, Tuple


@dataclass(frozen=True)
class HmmParameters:
    initial_probs: Tuple[float, ...]
    transition_matrix: Tuple[Tuple[float, ...], ...]
    emission_matrix: Tuple[Tuple[float, ...], ...]


@dataclass(frozen=True)
class ViterbiResult:
    states: Tuple[int, ...]
    log_probability: float
    forward_log_marginal: float
