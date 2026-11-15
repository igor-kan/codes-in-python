import math
from typing import List, Sequence
from exceptions import HmmDomainError
from models import HmmParameters, ViterbiResult


def _safe_log(p: float) -> float:
    return math.log(p) if p > 0.0 else -1.0e18


def log_sum_exp(values: Sequence[float]) -> float:
    m = max(values)
    if m <= -1.0e17:
        return m
    return m + math.log(sum(math.exp(v - m) for v in values))


class LogSpaceHmmDecoder:
    def decode(self, params: HmmParameters, observations: Sequence[int]) -> ViterbiResult:
        n_states = len(params.initial_probs)
        n_steps = len(observations)
        if n_steps == 0:
            raise HmmDomainError("observation sequence must be non-empty")

        dp: List[List[float]] = [[-1.0e18] * n_states for _ in range(n_steps)]
        bp: List[List[int]] = [[0] * n_states for _ in range(n_steps)]
        fwd: List[List[float]] = [[-1.0e18] * n_states for _ in range(n_steps)]

        o0 = observations[0]
        for s in range(n_states):
            lp = _safe_log(params.initial_probs[s]) + _safe_log(params.emission_matrix[s][o0])
            dp[0][s] = lp
            fwd[0][s] = lp

        for t in range(1, n_steps):
            obs = observations[t]
            for s in range(n_states):
                emit_lp = _safe_log(params.emission_matrix[s][obs])
                best_val = -1.0e30
                best_prev = 0
                cands = []
                for prev in range(n_states):
                    step_lp = _safe_log(params.transition_matrix[prev][s])
                    cand = dp[t - 1][prev] + step_lp
                    if cand > best_val:
                        best_val = cand
                        best_prev = prev
                    cands.append(fwd[t - 1][prev] + step_lp)
                dp[t][s] = best_val + emit_lp
                bp[t][s] = best_prev
                fwd[t][s] = log_sum_exp(cands) + emit_lp

        last = dp[-1]
        best_last = max(range(n_states), key=lambda s: last[s])
        path = [0] * n_steps
        path[-1] = best_last
        for t in range(n_steps - 1, 0, -1):
            path[t - 1] = bp[t][path[t]]
        return ViterbiResult(
            states=tuple(path),
            log_probability=last[best_last],
            forward_log_marginal=log_sum_exp(fwd[-1]),
        )
