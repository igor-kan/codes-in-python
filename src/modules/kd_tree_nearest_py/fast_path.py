from typing import List, Sequence


def linear_knn_dists(points: Sequence[Sequence[float]], query: Sequence[float], k: int) -> List[float]:
    dists = sorted(sum((x - y) ** 2 for x, y in zip(p, query)) for p in points)
    return dists[:k]
