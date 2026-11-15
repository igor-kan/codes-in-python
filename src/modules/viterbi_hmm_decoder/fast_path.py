import math
from typing import List, Sequence, Tuple
from models import HmmParameters


def compile_log_tables(
    params: HmmParameters,
) -> Tuple[List[float], List[List[float]], List[List[float]]]:
    tiny = -1.0e18
    init_l = [math.log(p) if p > 0.0 else tiny for p in params.initial_probs]
    trans_l = [[math.log(p) if p > 0.0 else tiny for p in row] for row in params.transition_matrix]
    emit_l = [[math.log(p) if p > 0.0 else tiny for p in row] for row in params.emission_matrix]
    return init_l, trans_l, emit_l


def decode_states_fast(params: HmmParameters, observations: Sequence[int]) -> List[int]:
    init_l, trans_l, emit_l = compile_log_tables(params)
    s_cnt = len(init_l)
    cur = [init_l[s] + emit_l[s][observations[0]] for s in range(s_cnt)]
    bp: List[List[int]] = []
    for t in range(1, len(observations)):
        obs = observations[t]
        nxt = [0.0] * s_cnt
        row_bp = [0] * s_cnt
        for s in range(s_cnt):
            best_v = -1.0e30
            best_p = 0
            for prev in range(s_cnt):
                val = cur[prev] + trans_l[prev][s]
                if val > best_v:
                    best_v = val
                    best_p = prev
            nxt[s] = best_v + emit_l[s][obs]
            row_bp[s] = best_p
        cur = nxt
        bp.append(row_bp)
    best_last = max(range(s_cnt), key=lambda s: cur[s])
    path = [best_last]
    for row_bp in reversed(bp):
        path.append(row_bp[path[-1]])
    path.reverse()
    return path
