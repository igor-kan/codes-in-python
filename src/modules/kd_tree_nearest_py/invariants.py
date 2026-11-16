from typing import Sequence
from core import KdTreeIndex
from exceptions import KdTreeDomainError
from fast_path import linear_knn_dists


def verify_knn_oracle(idx: KdTreeIndex, points: Sequence[Sequence[float]], query: Sequence[float], k: int) -> None:
    got = [h.dist_sq for h in idx.k_nearest(query, k)]
    oracle = linear_knn_dists(points, query, k)
    for g, o in zip(got, oracle):
        if abs(g - o) > 1e-9:
            raise KdTreeDomainError(f"kNN distance mismatch: got={got} oracle={oracle}")
