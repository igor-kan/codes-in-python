import math
from typing import Sequence
from exceptions import HmmDimensionError, HmmDomainError
from models import HmmParameters


def validate_hmm(params: HmmParameters, observations: Sequence[int]) -> None:
    s = len(params.initial_probs)
    if s <= 0:
        raise HmmDimensionError("state count must be positive")
    if len(params.transition_matrix) != s or len(params.emission_matrix) != s:
        raise HmmDimensionError("matrix row counts must equal initial_probs length")
    if not math.isclose(sum(params.initial_probs), 1.0, abs_tol=1e-7):
        raise HmmDomainError("initial probabilities must sum to 1.0")
    k_vocab = len(params.emission_matrix[0])
    for row in params.transition_matrix:
        if len(row) != s or not math.isclose(sum(row), 1.0, abs_tol=1e-7):
            raise HmmDomainError("transition rows must be valid stochastic vectors")
    for row in params.emission_matrix:
        if len(row) != k_vocab or not math.isclose(sum(row), 1.0, abs_tol=1e-7):
            raise HmmDomainError("emission rows must sum to 1.0")
    for obs in observations:
        if obs < 0 or obs >= k_vocab:
            raise HmmDomainError(f"observation index {obs} out of [0, {k_vocab})")
