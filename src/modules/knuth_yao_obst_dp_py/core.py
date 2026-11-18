from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def solve_obst(freq: List[int]) -> ObstSolution:
    n = len(freq)
    pref = [0] * (n + 1)
    for i, f in enumerate(freq):
        pref[i + 1] = pref[i] + f
    dp = [[0] * n for _ in range(n)]
    opt = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = freq[i]
        opt[i][i] = i
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            w = pref[j + 1] - pref[i]
            best = 10**18
            best_r = i
            for r in range(opt[i][j - 1], opt[i + 1][j] + 1):
                left = dp[i][r - 1] if r > i else 0
                right = dp[r + 1][j] if r < j else 0
                cand = left + right + w
                if cand < best:
                    best = cand; best_r = r
            dp[i][j] = best; opt[i][j] = best_r
    return ObstSolution(dp[0][n - 1], opt[0][n - 1])
