from typing import Dict, List, Optional, Tuple
import heapq
import math
from models import *
from exceptions import ValidationError

def levenshtein_with_trace(a: str, b: str) -> Tuple[int, List[str]]:
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            sub = dp[i - 1][j - 1] + (0 if a[i - 1] == b[j - 1] else 1)
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, sub)
    ops: List[str] = []
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + (0 if a[i - 1] == b[j - 1] else 1):
            ops.append("M" if a[i - 1] == b[j - 1] else "R")
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            ops.append("D")
            i -= 1
        else:
            ops.append("I")
            j -= 1
    ops.reverse()
    return dp[m][n], ops
