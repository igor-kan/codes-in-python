import bisect
from typing import List, Tuple
from models import JobInterval
from exceptions import IntervalDpValidationError


def solve_weighted_intervals(jobs: List[JobInterval]) -> Tuple[int, List[JobInterval]]:
    if not jobs:
        return 0, []
    for jb in jobs:
        if jb.start >= jb.end or jb.weight < 0:
            raise IntervalDpValidationError("invalid job interval")
    ordered = sorted(jobs, key=lambda x: x.end)
    ends = [jb.end for jb in ordered]
    n = len(ordered)
    dp = [0] * (n + 1)
    take = [False] * n
    prev_idx = [0] * n
    for i in range(n):
        p = bisect.bisect_right(ends, ordered[i].start, 0, i)
        prev_idx[i] = p
        with_i = ordered[i].weight + dp[p]
        if with_i > dp[i]:
            dp[i + 1] = with_i
            take[i] = True
        else:
            dp[i + 1] = dp[i]
    chosen: List[JobInterval] = []
    cur = n - 1
    while cur >= 0:
        if take[cur]:
            chosen.append(ordered[cur])
            cur = prev_idx[cur] - 1
        else:
            cur -= 1
    chosen.reverse()
    return dp[n], chosen
