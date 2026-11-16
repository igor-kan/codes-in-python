import random
from concurrency import batch_knn
from core import KdTreeIndex
from invariants import verify_knn_oracle


def run_properties() -> None:
    rng = random.Random(515)
    pts = [(rng.uniform(-50, 50), rng.uniform(-50, 50), rng.uniform(-50, 50)) for _ in range(150)]
    kd = KdTreeIndex(pts)
    qs = [(rng.uniform(-50, 50), rng.uniform(-50, 50), rng.uniform(-50, 50)) for _ in range(20)]
    for q in qs:
        verify_knn_oracle(kd, pts, q, 5)
    res = batch_knn(kd, qs, 5)
    assert all(len(r) == 5 for r in res)


if __name__ == "__main__":
    run_properties()
