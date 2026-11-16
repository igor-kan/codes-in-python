import itertools
from typing import Sequence


def small_exact_oracle(cost_matrix: Sequence[Sequence[float]]) -> float:
    r = len(cost_matrix)
    c = len(cost_matrix[0])
    best = float("inf")
    for perm in itertools.permutations(range(c), r):
        s = sum(cost_matrix[i][perm[i]] for i in range(r))
        if s < best:
            best = s
    return best
