from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def viterbi_log_path(init: List[float], trans: List[List[float]], emit: List[List[float]], obs: List[int]) -> Tuple[List[int], float]:
    n_s = len(init)
    n_t = len(obs)
    neg_inf = -1e18
    dp = [[neg_inf] * n_s for _ in range(n_t)]
    bp = [[0] * n_s for _ in range(n_t)]
    for s in range(n_s):
        if init[s] > 0.0 and emit[s][obs[0]] > 0.0:
            dp[0][s] = math.log(init[s]) + math.log(emit[s][obs[0]])
    for t in range(1, n_t):
        for s in range(n_s):
            if emit[s][obs[t]] <= 0.0:
                continue
            le = math.log(emit[s][obs[t]])
            for p in range(n_s):
                if trans[p][s] <= 0.0:
                    continue
                cand = dp[t - 1][p] + math.log(trans[p][s]) + le
                if cand > dp[t][s]:
                    dp[t][s] = cand
                    bp[t][s] = p
    last = max(range(n_s), key=lambda s: dp[-1][s])
    path = [0] * n_t
    path[-1] = last
    for t in range(n_t - 1, 0, -1):
        path[t - 1] = bp[t][path[t]]
    return path, dp[-1][last]
