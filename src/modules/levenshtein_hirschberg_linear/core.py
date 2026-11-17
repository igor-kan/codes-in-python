from typing import List, Tuple
from models import Alignment


def _nw_score(a: str, b: str) -> List[int]:
    prev = list(range(len(b) + 1))
    for ch in a:
        cur = [prev[0] + 1]
        for j, bch in enumerate(b, 1):
            cost = 0 if ch == bch else 1
            cur.append(min(cur[-1] + 1, prev[j] + 1, prev[j - 1] + cost))
        prev = cur
    return prev


def _hirschberg(a: str, b: str) -> Tuple[str, str]:
    n, m = len(a), len(b)
    if n == 0:
        return "-" * m, b
    if m == 0:
        return a, "-" * n
    if n == 1:
        best_j, best_cost = -1, m + 1
        for j, bch in enumerate(b):
            c = (0 if a[0] == bch else 1) + (m - 1)
            if c < best_cost:
                best_cost, best_j = c, j
        if m + 1 < best_cost:
            return "-" * m + a, b + "-"
        return "-" * best_j + a[0] + "-" * (m - 1 - best_j), b
    mid = n // 2
    score_l = _nw_score(a[:mid], b)
    score_r = _nw_score(a[mid:][::-1], b[::-1])[::-1]
    split = min(range(m + 1), key=lambda j: score_l[j] + score_r[j])
    al, bl = _hirschberg(a[:mid], b[:split])
    ar, br = _hirschberg(a[mid:], b[split:])
    return al + ar, bl + br


def align_hirschberg(a: str, b: str) -> Alignment:
    aa, bb = _hirschberg(a, b)
    dist = sum(1 for x, y in zip(aa, bb) if x != y)
    return Alignment(distance=dist, aligned_a=aa, aligned_b=bb)
