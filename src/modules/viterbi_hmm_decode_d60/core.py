from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def viterbi_decode(
    obs: List[int],
    init_p: List[float],
    trans_p: List[List[float]],
    emit_p: List[List[float]],
) -> HmmResult:
    if not obs or not init_p:
        raise ValidationError("observations and states must be non-empty")
    s = len(init_p)
    neg_inf = -1e18
    dp = [math.log(init_p[i]) + math.log(emit_p[i][obs[0]]) if init_p[i] > 0 and emit_p[i][obs[0]] > 0 else neg_inf for i in range(s)]
    back: List[List[int]] = []
    for o in obs[1:]:
        nxt = [neg_inf] * s
        b_row = [0] * s
        for j in range(s):
            em = math.log(emit_p[j][o]) if emit_p[j][o] > 0 else neg_inf
            best_v, best_i = neg_inf, 0
            for i in range(s):
                tr = math.log(trans_p[i][j]) if trans_p[i][j] > 0 else neg_inf
                cand = dp[i] + tr + em
                if cand > best_v:
                    best_v, best_i = cand, i
            nxt[j] = best_v
            b_row[j] = best_i
        dp = nxt
        back.append(b_row)
    last = max(range(s), key=lambda i: dp[i])
    path = [last]
    for b_row in reversed(back):
        last = b_row[last]
        path.append(last)
    path.reverse()
    return HmmResult(states=tuple(path), log_prob=max(dp))
