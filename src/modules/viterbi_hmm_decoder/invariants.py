from itertools import product
from typing import Sequence
from core import _safe_log
from models import HmmParameters, ViterbiResult


def path_log_prob(params: HmmParameters, obs: Sequence[int], states: Sequence[int]) -> float:
    total = _safe_log(params.initial_probs[states[0]]) + _safe_log(params.emission_matrix[states[0]][obs[0]])
    for t in range(1, len(obs)):
        total += _safe_log(params.transition_matrix[states[t - 1]][states[t]])
        total += _safe_log(params.emission_matrix[states[t]][obs[t]])
    return total


def verify_viterbi_optimality(params: HmmParameters, obs: Sequence[int], res: ViterbiResult) -> None:
    s_cnt = len(params.initial_probs)
    assert len(res.states) == len(obs)
    assert res.forward_log_marginal >= res.log_probability - 1e-9
    for brute_path in product(range(s_cnt), repeat=len(obs)):
        assert res.log_probability + 1e-9 >= path_log_prob(params, obs, brute_path)
